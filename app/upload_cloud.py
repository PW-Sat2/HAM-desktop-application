from threading import Thread, Event
import sys
import os
import time
import requests
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from libs.cloud import Cloud


class UploadCloud(Thread):
    def __init__(self, stop_event, config, cloud_tx_queue, cloud_rx_queue, error_queue, send_active):
        Thread.__init__(self)
        credentials_path = os.path.join(os.path.dirname(__file__), '..', config['CREDENTIALS_FILE'])
        base_url = config['CLOUD_URL']
        self.stop_event = stop_event
        self.cloud = Cloud(base_url, credentials_path)
        self.cloud_tx_queue = cloud_tx_queue
        self.cloud_rx_queue = cloud_rx_queue
        self.error_queue = error_queue
        self.send_active = send_active
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def run(self):
        while not self.stop_event.wait(0):
            if self.send_active.wait(1):
                try:
                    data = self.cloud_rx_queue.popleft()
                    try:
                        upload_result = self.cloud.put_packet(data.packet)
                        data.uuid = upload_result.uuid
                        data.upload_status = upload_result.status
                        self.cloud_tx_queue.appendleft(data)
                        if data.upload_status is False:
                            self.error_queue.appendleft(data)
                            self.logger.log(logging.DEBUG, "added to error queue because of credentials")
                    except requests.ConnectionError, requests.ReadTimeout:
                        data.upload_status = False
                        self.error_queue.appendleft(data)
                        self.cloud_tx_queue.appendleft(data)
                        self.logger.log(logging.DEBUG, "added to error queue because of internet")
                except IndexError:
                    time.sleep(1)
        self.logger.log(logging.DEBUG, "Finished UploadCloud")


class UploadCloudError(Thread):
    def __init__(self, stop_event, config, cloud_tx_queue, error_queue):
        Thread.__init__(self)
        credentials_path = os.path.join(os.path.dirname(__file__), '..', config['CREDENTIALS_FILE'])
        base_url = config['CLOUD_URL']
        self.stop_event = stop_event
        self.cloud = Cloud(base_url, credentials_path)
        self.cloud_tx_queue = cloud_tx_queue
        self.error_queue = error_queue
        self.error_buffer = []
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def run(self):
        while len(self.error_queue) != 0 and not self.stop_event.wait(0):
            self.error_buffer.append(self.error_queue.popleft())

        while not self.stop_event.wait(0) and len(self.error_buffer) > 0:
            data = self.error_buffer.pop()
            try:
                upload_result = self.cloud.put_packet(data.packet)
                data.uuid = upload_result.uuid
                data.upload_status = upload_result.status
                self.cloud_tx_queue.append(data)
                if data.upload_status is False:
                    self.error_queue.appendleft(data)
                    print "again added to error queue"
            except IndexError:
                time.sleep(1)
            except requests.ConnectionError:
                self.error_queue.appendleft(data)
                print "again added to error queue"

        self.logger.log(logging.DEBUG, "Finished UploadCloudError")

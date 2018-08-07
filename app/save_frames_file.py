from threading import Thread
import Queue
import sys
import os
import time
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from libs.frame_file import FrameFile
import logging


class SaveFramesFileThread(Thread):
    def __init__(self, stop_event, config, file_queue, path_queue):
        Thread.__init__(self)
        self.stop_event = stop_event
        self.file_queue = file_queue
        self.config = config
        self.first_packet = True
        self.path_queue = path_queue
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def __generate_path(self):
        base = self.config['DEFAULT_SAVE_DIR']
        filename = datetime.datetime.utcfromtimestamp(time.time()).strftime("%Y-%m-%d_%H-%M-%S-%f")
        return "{0}/{1}_PW-Sat2_Downlink_Frames.frames".format(base, filename)

    def __send_path(self, path):
        self.path_queue.put(path)

    def run(self):
        writer = None
        while not self.stop_event.wait(0):
            try:
                data = self.file_queue.get(block=True, timeout=1)

                if self.first_packet:
                    self.first_packet = False
                    path = self.__generate_path()
                    self.__send_path(path)
                    writer = FrameFile(path)

                writer.save(data)
            except Queue.Empty:
                pass
        self.logger.log(logging.DEBUG, "Finished ReceiveDistribute")

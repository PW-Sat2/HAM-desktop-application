from threading import Thread
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from libs.receiver import Receiver
import logging


class ReceiveDistribute(Thread):
    def __init__(self, stop_event, config, gui_queue, file_queue):
        Thread.__init__(self)
        self.target = config['ZMQ_TARGET']
        self.port = config['ZMQ_PORT']
        self.stop_event = stop_event
        self.rcv = Receiver(self.target, self.port)
        self.rcv.set_timeout(1000)
        self.gui_queue = gui_queue
        self.file_queue = file_queue
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def connect_and_get_packet(self):
        try:
            packet = self.rcv.get_packet()
            return packet
        except:
            return None

    def run(self):
        while not self.stop_event.wait(0):
            packet = self.connect_and_get_packet()
            if packet is not None:
                self.gui_queue.append(packet)
                self.file_queue.put(packet)
        self.logger.log(logging.DEBUG, "Finished ReceiveDistribute")

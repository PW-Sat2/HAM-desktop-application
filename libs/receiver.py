import time
import zmq
import logging

class Receiver:
    def __init__(self, target="localhost", port=7001):
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.SUB)
        self.sock.connect("tcp://%s:%d" % (target, port))
        self.sock.setsockopt(zmq.SUBSCRIBE, "")
        self.set_timeout(-1)
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    """Set timeout on socket.
        -1 for infinity"""
    def set_timeout(self, timeout_in_ms=-1):
        self.sock.setsockopt(zmq.RCVTIMEO, timeout_in_ms)

    class TimeoutError(Exception):
        pass

    """ Receive RAW frame from socket. If timeout expired zmq.Again is raised """
    def receive_raw(self):
        return self.sock.recv()

    def get_packet(self):
        frame_data = self.receive_raw()
        return {'timestamp': time.time(), 'frame': frame_data}


def connect_and_get_packet(target="localhost", port=7001):
    rcv = Receiver(target, port)
    return rcv.get_packet()

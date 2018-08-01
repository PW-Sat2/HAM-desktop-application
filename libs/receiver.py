import imp
import os
import sys
import time

import zmq
from zmq.utils.win32 import allow_interrupt
from utils import ensure_string


class Receiver:
    def __init__(self, target="localhost", port=7001):
        self.context = zmq.Context.instance()
        self.sock = self.context.socket(zmq.SUB)
        self.sock.connect("tcp://%s:%d" % (target, port))
        self.sock.setsockopt(zmq.SUBSCRIBE, "")
        self.timeout(-1)
        self.abort_send = self.context.socket(zmq.PAIR)
        self.abort_recv = self.context.socket(zmq.PAIR)

        self.abort_send.bind('inproc://receiver/abort')
        self.abort_recv.connect('inproc://receiver/abort')

    def timeout(self, timeout_in_ms=-1):
        self.set_timeout = timeout_in_ms
        self.sock.setsockopt(zmq.RCVTIMEO, self.set_timeout)

    def receive(self):
        while self.receive_no_wait() is not None:
            pass

        def stop():
            self.abort_send.send('QUIT')

        self._flush_socket(self.abort_recv, -1)

        with allow_interrupt(stop):
            (read, _, _) = zmq.select([self.sock, self.abort_recv], [], [self.sock, self.abort_recv])

            if read[0] == self.sock:
                return ensure_string(self.sock.recv())
            elif read[0] == self.abort_recv:
                return None
            else:
                return None

    def receive_no_wait(self):
        self.sock.setsockopt(zmq.RCVTIMEO, 0)
        val = None
        try:
            val = self.sock.recv()
        except zmq.Again:
            pass
        finally:
            self.sock.setsockopt(zmq.RCVTIMEO, self.set_timeout)
            return val

    def get_packet(self):
        frame_data = self.receive()
        return {'timestamp': time.time(), 'frame': frame_data}

    def _flush_socket(self, socket, timeout):
        socket.setsockopt(zmq.RCVTIMEO, 0)

        while True:
            try:
                socket.recv()
            except zmq.Again:
                break

        socket.setsockopt(zmq.RCVTIMEO, timeout)


def connect_and_get_packet(target="localhost", port=7001):
    rcv = Receiver(target, port)
    return rcv.get_packet()

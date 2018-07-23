import zmq
import logging


class FrameSink:
    def __init__(self, address="tcp://*:7001"):
        self.address = address
        self.logger = logging.getLogger("ZMQS")

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.logger.log(logging.DEBUG, "Address: |{0}|".format(address))
        self.socket.bind(address)

    def sink(self, data):
        self.socket.send(data)
        self.logger.log(logging.DEBUG, "Data frame sent!")


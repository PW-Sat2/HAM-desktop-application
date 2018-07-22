import zmq

class FrameSink:
    def __init__(self, address="tcp://*:7001"):
        self.address = address

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        print "Address: |%s|" % address
        self.socket.bind(address)

    def sink(self, data):
        self.socket.send(data)

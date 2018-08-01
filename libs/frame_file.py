import base64
import time
import datetime
import logging


class FrameFile:
    def __init__(self, path):
        self.path = path
        self.logger = logging.getLogger("FrameFile")

    def __format_timestamp(self, packet):
        return datetime.datetime.fromtimestamp(packet["timestamp"]).strftime("%Y-%m-%d_%H:%M:%S:%f")

    def __decode_timestamp(self, timestamp_string):
        return time.mktime(datetime.datetime.strptime(timestamp_string, "%Y-%m-%d_%H:%M:%S:%f").timetuple())

    def __encode_base64(self, packet):
        return base64.b64encode(packet["frame"])

    def __decode_base64(self, frame):
        return base64.b64decode(frame)

    def __decode(self, raw):
        split_raw = raw.split(',')
        return {'timestamp': self.__decode_timestamp(split_raw[0]), 'frame': self.__decode_base64(split_raw[2])}

    def save(self, packet):
        with open(self.path, "a") as f:
            f.write(self.__format_timestamp(packet) + "," + "D" + "," + self.__encode_base64(packet) + "\n")
        self.logger.log(logging.DEBUG, "Frame saved to file " + str(self.path))

    def read_raw(self):
        with open(self.path, "r") as f:
            return f.readlines()

    def read_packets(self):
        raw = self.read_raw()
        packets = []
        for item in raw:
            try:
                packets.append(self.__decode(item))
                self.logger.log(logging.DEBUG, "Processed packet: " + item)
            except ValueError:
                self.logger.log(logging.DEBUG, "ValueError in packet decoding: " + item)
            except TypeError:
                self.logger.log(logging.DEBUG, "TypeError in packet decoding: " + item)
        return packets

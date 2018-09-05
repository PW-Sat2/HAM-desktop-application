import base64
import datetime
import logging


class FrameFile:
    def __init__(self, path):
        self.path = path
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def __format_timestamp(self, packet):
        return datetime.datetime.utcfromtimestamp(packet["timestamp"]).strftime("%Y-%m-%d_%H:%M:%S:%f")

    def __decode_timestamp(self, timestamp_string):
        return (datetime.datetime.strptime(timestamp_string, "%Y-%m-%d_%H:%M:%S:%f") -
                datetime.datetime.utcfromtimestamp(0)).total_seconds()

    def __encode_base64(self, packet):
        return base64.b64encode(packet["frame"])

    def __decode_base64(self, frame):
        return base64.b64decode(frame)

    def __decode(self, raw):
        split_raw = raw.split(',')

        if len(split_raw) != 3:
            raise ValueError('Corrupted file line/frame', len(split_raw))

        return {'timestamp': self.__decode_timestamp(split_raw[0]), 'frame': self.__decode_base64(split_raw[2])}

    def save(self, packet):
        with open(self.path, "a") as f:
            packet_string = ','.join([self.__format_timestamp(packet), 'D', self.__encode_base64(packet)])
            f.write(packet_string + '\n')
        self.logger.log(logging.DEBUG, "Frame saved to file " + str(self.path))

    def read_raw(self):
        with open(self.path, "r") as f:
            return f.readlines()

    def read_packets(self):
        try:
            raw = self.read_raw()
            packets = []
            for item in raw:
                try:
                    packets.append(self.__decode(item))
                    self.logger.log(logging.DEBUG, "Processed packet: " + item)
                except ValueError as error:
                    self.logger.log(logging.DEBUG, "ValueError " + str(error.args) + " in packet decoding: " + item)
                except TypeError as error:
                    self.logger.log(logging.DEBUG, "TypeError " + str(error.args) + " in packet decoding: " + item)
            return packets
        except IOError:
            return None

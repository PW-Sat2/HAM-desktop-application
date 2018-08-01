import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../libs'))
from frame_file import *

frame_file = open('../test_frames/frame_0.raw', "rb")
frame_data = frame_file.read()
timestamp = 1534564313.345
packet = {'timestamp': timestamp, 'frame': frame_data}
frame_file_reference = "2018-08-18_03:51:53:345000,D,oK6mgqhk4KCupoKoZGED8M0CAAAAB2YAwjcsvpcFAAAAAODabjgAAAAAAAAAA" \
                       "AAAAAAAAAAMvAIA1wkAgeMNAAAAAAAAAAAAAAAAAAAAAACA/P/1fwKAOG/JCSrkdqecsAFgAFA5cVUqx1NKNmHQm71" \
                       "HdyI9AAUq4GqrKAYQAFdbjuiAANjaukXBiAPcTAHgtxOAFjoeVYgKAA8AZHMBABdX7KLGGuuTJ8ADQCYKAEDGF8cIA" \
                       "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOBY="


class TestFrameFile(unittest.TestCase):
    def test_save(self):
        saver = FrameFile('test.frames')
        saver.save(packet)
        with open('test.frames', 'rb') as f:
            saved_data = f.readlines()[-1]
            self.assertEqual(saved_data.strip(), frame_file_reference.strip())

    def test_read_raw(self):
        reader = FrameFile('test.frames')
        raw_line = reader.read_raw()[-1]
        self.assertEqual(raw_line.strip(), frame_file_reference.strip())

    def test_read_packet(self):
        reader = FrameFile('test.frames')
        read_packet = reader.read_packets()[-1]
        self.assertEqual(read_packet, packet)

    def test_read_qty_of_packets(self):
        reader = FrameFile('test.frames')
        read_packet_qty = len(reader.read_packets())
        with open('test.frames', 'rb') as f:
            reference_packet_qty = len(f.readlines())
            self.assertEqual(read_packet_qty, reference_packet_qty)

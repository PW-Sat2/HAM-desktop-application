import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../libs'))
from frame_recognizer import FrameRecognizer

matched_apids = [(0x01, "pong"),
                  (0x02, "operation"),
                  (0x03, "error counters"),
                  (0x04, "program upload"),
                  (0x05, "periodic message"),
                  (0x06, "persistent state"),
                  (0x07, "boot slots info"),
                  (0x08, "compile info"),
                  (0x09, "erase flash"),
                  (0x0A, "file remove"),
                  (0x0B, "file send"),
                  (0x0C, "file list"),
                  (0x0D, "telemetry"),
                  (0x0E, "photo"),
                  (0x0F, "suns"),
                  (0x10, "experiment"),
                  (0x11, "error counter configuration"),
                  (0x12, "purge photo"),
                  (0x13, "power cycle"),
                  (0x14, "sail"),
                  (0x15, "time correction"),
                  (0x16, "time set"),
                  (0x17, "comm"),
                  (0x18, "set bitrate"),
                  (0x19, "disable overheat submode"),
                  (0x1A, "i2c"),
                  (0x1B, "periodic set"),
                  (0x1C, "sail experiment")]

matched_frames = [("frame_0.raw", 0xCD),
                  ("frame_5.raw", 0x0C),
                  ("frame_6.raw", 0x0B),
                  ("frame_7.raw", 0x4B),
                  ("frame_8.raw", 0x8B),
                  ("frame_9.raw", 0xCB)]

frame_folder = '../test_frames/'

class TestFrameRecognizer(unittest.TestCase):
    def test_frame_telemetry(self):
        apid_byte = 0xCD
        self.assertEqual(FrameRecognizer.match_apid(apid_byte), "telemetry")

    def test_frames(self):
        for pair in matched_apids:
            self.assertEqual(FrameRecognizer.match_apid(pair[0]), pair[1])

    def test_frames_shifted_last_bit(self):
        for pair in matched_apids:
            self.assertEqual(FrameRecognizer.match_apid(pair[0] + 0x80), pair[1])

    def test_frames_shifted_last_two_bits(self):
        for pair in matched_apids:
            self.assertEqual(FrameRecognizer.match_apid(pair[0] + 0xC0), pair[1])

    def test_frame_file_unknown(self):
        for apid_byte in range(0xDD, 0xFF):
            self.assertEqual(FrameRecognizer.match_apid(apid_byte), "unknown")

    def test_frame_apid(self):
        for pair in matched_frames:
            with open(frame_folder + pair[0], "rb") as f:
                frame_data = f.read()
                self.assertEqual(FrameRecognizer.get_apid(frame_data), pair[1])

import sys
import os
import unittest
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '../libs'))
from cloud import *

baseUrl = "http://titan.gajoch.pl:9090"
credentialsPath = "credentials.json"
cloud = Cloud(baseUrl, credentialsPath)

frame_file = open('../test_frames/frame_0.raw', "rb")
frame_data = frame_file.read()
timestamp = 1534564313.345
packet = {'timestamp': timestamp, 'frame': frame_data}


class TestCloud(unittest.TestCase):
    def test_base_url(self):
        self.assertEqual(cloud.base_url, baseUrl)

    def test_auth(self):
        self.assertEqual(cloud.validate_auth(cloud.authenticate()), True)

    def test_put_frame_status(self):
        res = cloud.put_packet(packet)
        self.assertEqual(res.status, True)

    def test_put_frame_uuid(self):
        res = cloud.put_packet(packet)
        self.assertGreaterEqual(len(res.uuid), 13)

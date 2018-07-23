import time
import random
import glob
import logging


class FrameFactory:
    def __init__(self, frames_directory):
        self.frames_directory = frames_directory
        self.frames_list = self.get_frames_list()
        self.logger = logging.getLogger("FF  ")

    def get_frames_list(self):
        return glob.glob(self.frames_directory + "/*.raw")

    def get_random_frame(self):
        frame_no = random.randrange(0, len(self.frames_list)-1)
        frame_path = self.frames_list[frame_no]
        self.logger.log(logging.DEBUG, "Frame path: {0}".format(frame_path))
        with open(frame_path, 'rb') as frame:
            return frame.read()

    def random_sleep(self, min_interval=0.01, max_interval=1):
        time_to_sleep = random.uniform(min_interval, max_interval)
        self.logger.log(logging.DEBUG, "Sleeping: {0} s".format(time_to_sleep))
        time.sleep(time_to_sleep)
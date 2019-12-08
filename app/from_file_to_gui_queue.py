import sys
import os
from PyQt4 import QtGui

from threading import Thread
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from libs.frame_file import FrameFile
import logging


class FromFileToGuiQueueThreadFactory:
    def __init__(self, stop_event, config, gui_queue):
        self.gui_queue = gui_queue
        self.stop_event = stop_event
        self.default_dir = config['DEFAULT_SAVE_DIR']
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def load_from_file(self):
        try:
            file_dialog = QtGui.QFileDialog()
            path = file_dialog.getOpenFileName(None, 'OpenFile', self.default_dir, "Frames file (*.frames)")
            self.logger.log(logging.DEBUG, "Selected file: " + path)
            thread = FromFileToGuiQueueThread(self.stop_event, FrameFile(path), self.gui_queue)
            thread.start()
            thread.join()
        except:
            self.logger.log(logging.ERROR, "Load file exception")


class FromFileToGuiQueueThread(Thread):
    def __init__(self, stop_event, reader, gui_queue):
        Thread.__init__(self)
        self.gui_queue = gui_queue
        self.stop_event = stop_event
        self.reader = reader
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def run(self):
        self.logger.log(logging.DEBUG, "Starting thread FromFileToGuiQueueThread")
        packets = self.reader.read_packets()
        try:
            for packet in packets:
                self.gui_queue.append(packet)
        except TypeError:
            self.logger.log(logging.ERROR, "Empty packets list")
        self.logger.log(logging.DEBUG, "Finished FromFileToGuiQueueThread")

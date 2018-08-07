from PyQt4 import QtGui
import Queue
import logging


class ExitMessageHandler:
    def __init__(self, gui_queue, cloud_tx_queue, cloud_rx_queue, error_queue, path_queue):
        self.gui_queue = gui_queue
        self.cloud_tx_queue = cloud_tx_queue
        self.cloud_rx_queue = cloud_rx_queue
        self.error_queue = error_queue
        self.file_path = None
        self.path_queue = path_queue
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def queues_empty(self):
        return len(self.gui_queue) == 0 and \
               len(self.cloud_tx_queue) == 0 and \
               len(self.cloud_rx_queue) == 0 and \
               len(self.error_queue) == 0

    def __get_path(self):
        try:
            self.file_path = self.path_queue.get(block=True, timeout=1)
        except Queue.Empty:
            pass

    def saved_file(self):
        return self.file_path is not None

    def __window_not_all_sent(self, event, with_file):
        quit_msg = "Not all frames have been uploaded to cloud.<br>" \
                   "Are you sure you want to exit the program?"

        if with_file:
            quit_msg = quit_msg + "<br>You can upload frames later from file: {0}".format(self.file_path)

        popup_reply = QtGui.QMessageBox.question(None, 'Confirm exit',
                                                 quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if popup_reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def __window_saved_frames(self, event):
        quit_msg = "Frames from this communication session have been saved to file: {0}".format(self.file_path)

        QtGui.QMessageBox.information(None, 'Information',
                                      quit_msg, QtGui.QMessageBox.Ok)
        event.accept()

    def exit_action(self, event):
        self.__get_path()

        if not self.queues_empty():
            self.__window_not_all_sent(event, self.saved_file())
        elif self.saved_file():
            self.__window_saved_frames(event)

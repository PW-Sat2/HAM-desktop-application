from PyQt4 import QtCore
import time
import logging


class GetFromQueueToSignalThread(QtCore.QThread):

    item_ready = QtCore.pyqtSignal(object)

    def __init__(self, stop_event, timeout, gui_queue):
        QtCore.QThread.__init__(self)
        self.gui_queue = gui_queue
        self.stop_event = stop_event
        self.timeout = timeout
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def run(self):
        while not self.stop_event.wait(self.timeout):
            try:
                widget_item = self.gui_queue.pop()
                self.item_ready.emit(widget_item)
            except IndexError:
                time.sleep(1)
            except Exception as e:
                self.logger.error("Major Exception in GetFromQueueToSignalThread", exc_info=e)
        self.logger.log(logging.DEBUG, "Finished GetFromQueueToSignalThread")

from PyQt4 import QtCore, QtGui
from libs.cloud import Cloud
import logging
import os


class CheckAuthThread(QtCore.QThread):

    state_signal = QtCore.pyqtSignal(object)

    def __init__(self, stop_event, config):
        QtCore.QThread.__init__(self)
        self.stop_event = stop_event
        self.cloud = Cloud(config['CLOUD_URL'], os.path.join(os.path.dirname(__file__), '..', config['CREDENTIALS_FILE']))
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def check(self):
        try:
            auth_res = self.cloud.authenticate()
            self.state_signal.emit(self.cloud.validate_auth(auth_res))
        except:
            self.state_signal.emit(False)

    def run(self):
        self.check()
        while not self.stop_event.wait(30):
            try:
                self.check()
            except Exception as e:
                self.logger.error("Major Exception in Check Auth hread", exc_info=e)
        self.logger.log(logging.DEBUG, "Finished CheckAuthThread")

from PyQt4 import QtCore, QtGui
from libs.cloud import Cloud
import ping
import logging


class CheckAuthThread(QtCore.QThread):

    state_signal = QtCore.pyqtSignal(object)

    def __init__(self, stop_event, config):
        QtCore.QThread.__init__(self)
        self.stop_event = stop_event
        self.cloud = Cloud(config['CLOUD_URL'], config['CREDENTIALS_FILE'])
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def check(self):
        try:
            auth_res = self.cloud.authenticate()
            self.state_signal.emit(self.cloud.validate_auth(auth_res))
            print self.cloud.validate_auth(auth_res)
        except:
            self.state_signal.emit(False)
            print "False except"

    def run(self):
        self.check()
        while not self.stop_event.wait(30):
            self.check()
        self.logger.log(logging.DEBUG, "Finished CheckAuthThread")


class CheckOnlineThread(QtCore.QThread):

    state_signal = QtCore.pyqtSignal(object)

    def __init__(self, stop_event, config):
        QtCore.QThread.__init__(self)
        self.server = config['PING_URL']
        self.stop_event = stop_event
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def __check(self):
        try:
            ping.do_one(self.server, 1, 1)
            self.state_signal.emit(True)
        except:
            self.state_signal.emit(False)
            pass

    def run(self):
        self.__check()
        while not self.stop_event.wait(30):
            self.__check()
        self.logger.log(logging.DEBUG, "Finished CheckOnlineThread")

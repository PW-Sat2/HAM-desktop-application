import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from PyQt4 import QtCore, QtGui
import logging
import webbrowser
import imp
import urllib
import time


class Updater(QtCore.QThread):

    to_update = QtCore.pyqtSignal(object)

    def __init__(self, stop_event, config, application_path):
        QtCore.QThread.__init__(self)
        self.config = config
        self.stop_event = stop_event
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self.application_path = application_path

    def download_version_file(self):
        got_version_file = False
        while not got_version_file and not self.stop_event.wait(0):
            try:
                urllib.urlretrieve(self.config['APP_NEW_VERSION_URL'], 'current_version.py')
                got_version_file = True
            except:
                got_version_file = False
                self.logger.log(logging.DEBUG, "Error in getting version file")
                time.sleep(10)
        self.logger.log(logging.DEBUG, "Got version file")

    def is_new_version_available(self):
        app_version = self.config['APP_VERSION']
        app_new_version = self.new_version_desc.new_version['APP_NEW_VERSION']
        if app_new_version > app_version:
            self.to_update.emit(True)
            self.logger.log(logging.DEBUG, "New version available")

    def load_new_version_desc(self):
        self.new_version_desc = imp.load_source('new_version_desc', os.path.join(self.application_path,
                                                                                 'current_version.py'))

    def show_update_window(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)

        msg.setText(self.new_version_desc.new_version['WINDOW_TEXT'])
        msg.setInformativeText(self.new_version_desc.new_version['WINDOW_INFORMATIVE_TEXT'])
        msg.setWindowTitle(self.new_version_desc.new_version['WINDOW_TITLE'])
        msg.setDetailedText(self.new_version_desc.new_version['WINDOW_DETAILED_TEXT'])

        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgbtn)

        retval = msg.exec_()
        self.logger.log(logging.DEBUG, "Value of pressed update message box button: {0}".format(retval))

    def msgbtn(self, response):
        self.logger.log(logging.DEBUG, response.text())
        if str(response.text()).find("OK") != -1:
            webbrowser.open(self.new_version_desc.new_version['UPDATE_URL'])
            self.logger.log(logging.DEBUG, "Web browser opened")

    def run(self):
        self.download_version_file()
        self.load_new_version_desc()
        self.is_new_version_available()
        self.logger.log(logging.DEBUG, "Finished Updater")

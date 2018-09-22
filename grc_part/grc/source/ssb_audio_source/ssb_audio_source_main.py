from PyQt4 import QtGui
import os
import sys
from PyQt4 import QtGui
import time

from PyQt4 import QtCore
import time
import logging
import subprocess
import ssb_audio_source
from parameters_window import Ui_Dialog

class ParamshWrapper:
    def __init__(self, audio_dev, samp_rate, frequency):
        self.audio_dev = str(audio_dev)
        self.samp_rate = int(samp_rate)
        self.frequency = int(frequency)
        print self.samp_rate
        print self.frequency


class SSBAudioSource(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ok = False
        self.ui.buttonBox.accepted.connect(self.accept_set)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept_set(self):
        self.ok = True

    def params(self):
        return ParamshWrapper(self.ui.audio_dev.text(), self.ui.sampling_rate.value(), self.ui.frequnecy_offset.value())

    def closeEvent(self, event):
        pass


def run_grc(params):
    ssb_audio_source.main(options=params)

def error_popup():
    error_window = QtGui.QMessageBox()
    error_window.setIcon(QtGui.QMessageBox.Critical)
    error_window.setText('You have to accept (click "OK") pop-up window!')
    error_window.setInformativeText(
        "Audio in source will close now - run it again and accept pop-up window with parameters!")
    error_window.setWindowTitle("Accept pop-up with parameters!")
    error_window.setDetailedText("")
    error_window.setStandardButtons(QtGui.QMessageBox.Ok)
    error_window.exec_()


def application():
    dialog = QtGui.QApplication(sys.argv)
    params_dialog = SSBAudioSource()
    params_dialog.show()
    result = dialog.exec_()
    print params_dialog.ok
    if params_dialog.ok:
        run_grc(params_dialog.params())
    else:
        error_popup()
    sys.exit()


if __name__ == "__main__":
    application()

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

class ParamshWrapper:
    def __init__(self, audio_dev):
        self.audio_dev = str(audio_dev)


class SSBAudioSource(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.dialog()

    def dialog(self):
        audio, ok = QtGui.QInputDialog.getText(self, 'Enter audio device name...', 'Enter audio device name (or just '
                                                                                  'leave empty field to use default '
                                                                                  'device):')

        if ok:
            ssb_audio_source.main(options=ParamshWrapper(audio))

    def closeEvent(self, event):
        pass


def application():
    app = QtGui.QApplication(sys.argv)
    window = SSBAudioSource()
    sys.exit()


if __name__ == "__main__":
    application()

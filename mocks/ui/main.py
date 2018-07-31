import sys
from PyQt4 import QtCore, QtGui
from main_window import Ui_mainWindow
from frame_list_element import UiFrameListWidget


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.i = 0
        self.j = 0

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.init_list()
        self.init_ribbon()

    def init_ribbon(self):
        self.ui.serverConnectionStatusTextLabel.setToolTip("Server radio.pw-sat.pl is online")
        self.ui.serverConnectionStatusTextLabel.setText("Online")
        self.ui.credentialsButton.setText("michal.gumiela@gmail.com")
        self.ui.serverConnectionStatusIconLabel.setToolTip("Server radio.pw-sat.pl is online")

    def init_list(self):
        for i in range(100):
            item_widget = UiFrameListWidget()

            item_widget.uuidValueLabel.setText('<a style="color: #414141;" href="http://titan.gajoch.pl:9090/telemetry/'
                                               'detailed/frame/14016296-8d4f-4a25-8911-5ecaeb13d9ff">'
                                               '14016296-8d4f-4a25-8911-5ecaeb13d9ffp</a>')
            item_widget.uuidValueLabel.setOpenExternalLinks(True)
            item_widget.uploadStatusIconButton.setToolTip("Frame successfully sent to server, thanks!")
            item_widget.timestampLabel.setText("10:53:13.224 2017-02-15")

            if (self.j % 2) == 0:
                item_widget.frameTypeLabel.setStyleSheet('background-color:#2196f3; color:#ffffff; border: none;'
                                                         'font-weight: bold;')
                item_widget.frameTypeLabel.setText('error counter configuration')
            else:
                item_widget.frameTypeLabel.setStyleSheet('background-color:#4CAF50; color:#ffffff; border: none;'
                                                         'font-weight: bold;')
                item_widget.frameTypeLabel.setText('pong')
            self.j += 1

            item = QtGui.QListWidgetItem(self.ui.framesListWidget)
            item.setSizeHint(QtCore.QSize(0, 65))
            self.ui.framesListWidget.addItem(item)
            self.ui.framesListWidget.setItemWidget(item, item_widget)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    hamApp = StartQT4()
    hamApp.show()
    sys.exit(app.exec_())
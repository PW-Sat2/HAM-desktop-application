import sys
from PyQt4 import QtGui, QtCore
from main_window import Ui_mainWindow
import list_element2 as list_element

reload(list_element)


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.i = 0
        self.j = 0

        self.ui.pushButton.pressed.connect(self.update)

        self.copy_list = []

        for i in range(10):
            item = QtGui.QListWidgetItem(self.ui.listWidget)
            self.copy_list.append(item)
            item_widget = list_element.Ui_self()
            item_widget.label_uuid_value.setText('<a style="color: #414141;" href="http://titan.gajoch.pl:9090/telemetry/detailed/frame/14016296-8d4f-4a25-8911-5ecaeb13d9ff">14016296-8d4f-4a25-8911-5ecaeb13d9ffp</a>')
            item_widget.label_uuid_value.setOpenExternalLinks(True)
            item.setSizeHint(QtCore.QSize(0, 65))
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, item_widget)
                   

            if (self.j % 2) == 0:
                item_widget.label_frame_type.setStyleSheet('background-color:#2196f3; color:#ffffff; border: none; font-weight: bold;')
                item_widget.label_frame_type.setText('error counter configuration')
            else:
                item_widget.label_frame_type.setStyleSheet('background-color:#4CAF50; color:#ffffff; border: none; font-weight: bold;')
                item_widget.label_frame_type.setText('pong')
            self.j += 1          

    def update(self):
        item_widget = list_element.Ui_self()
        item_widget.label_uuid_value.setText('<a style="color: #414141;" href="http://titan.gajoch.pl:9090/telemetry/detailed/frame/14016296-8d4f-4a25-8911-5ecaeb13d9ff">dupa</a>')
        item_widget.label_uuid_value.setOpenExternalLinks(True)
        self.ui.listWidget.setItemWidget(self.copy_list[self.i], item_widget)
        self.i += 1



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
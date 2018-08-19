from PyQt4 import QtGui


def set_btn_icon(btn, icon_path):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    btn.setIcon(icon)

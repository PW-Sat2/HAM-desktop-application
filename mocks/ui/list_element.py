# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\list_element.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_self(QtGui.QWidget):
    def __init__ (self, parent = None):
        super(QtGui.QWidget, self).__init__(parent)
        self.label_uuid_text = QtGui.QLabel(self)
        self.label_uuid_text.setGeometry(QtCore.QRect(54, 40, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_uuid_text.setFont(font)
        self.label_uuid_text.setObjectName(_fromUtf8("label_uuid_text"))
        self.label_uuid_value = QtGui.QLabel(self)
        self.label_uuid_value.setGeometry(QtCore.QRect(92, 40, 341, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_uuid_value.setFont(font)
        self.label_uuid_value.setScaledContents(False)
        self.label_uuid_value.setWordWrap(False)
        self.label_uuid_value.setOpenExternalLinks(True)
        self.label_uuid_value.setObjectName(_fromUtf8("label_uuid_value"))
        self.label_timestamp = QtGui.QLabel(self)
        self.label_timestamp.setGeometry(QtCore.QRect(54, 12, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_timestamp.setFont(font)
        self.label_timestamp.setObjectName(_fromUtf8("label_timestamp"))
        self.downlink_icon = QtGui.QLabel(self)
        self.downlink_icon.setGeometry(QtCore.QRect(10, 21, 30, 30))
        self.downlink_icon.setText(_fromUtf8(""))
        self.downlink_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/downlink-green/downlink-color-green.png")))
        self.downlink_icon.setObjectName(_fromUtf8("downlink_icon"))
        self.upload_status_icon = QtGui.QLabel(self)
        self.upload_status_icon.setGeometry(QtCore.QRect(450, 21, 30, 30))
        self.upload_status_icon.setText(_fromUtf8(""))
        self.upload_status_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/cloud-online/cloud-online.png")))
        self.upload_status_icon.setObjectName(_fromUtf8("upload_status_icon"))
        self.label_frame_type = QtGui.QPushButton(self)
        self.label_frame_type.setGeometry(QtCore.QRect(220, 12, 213, 20))
        self.label_frame_type.setAutoFillBackground(False)
        self.label_frame_type.setObjectName(_fromUtf8("label_frame_type"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.label_uuid_text.setText(_translate("Form", "uuid:", None))
        self.label_uuid_value.setToolTip(_translate("Form", "Click to see the frame content", None))
        self.label_uuid_value.setText(_translate("Form", "14016296-8d4f-4a25-8911-5ecaeb13d9ffp", None))
        self.label_timestamp.setToolTip(_translate("Form", "Timestamp", None))
        self.label_timestamp.setText(_translate("Form", "2017-11-30 11:14:33", None))
        self.downlink_icon.setToolTip(_translate("Form", "Downlink", None))
        self.upload_status_icon.setToolTip(_translate("Form", "Frame successfully sent to server, thanks!", None))
        self.label_frame_type.setText(_translate("Form", "PushButton", None))

import img_pix_rc

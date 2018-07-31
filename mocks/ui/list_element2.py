# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\list_element2.ui'
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
        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -2, 501, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.downlink_icon = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downlink_icon.sizePolicy().hasHeightForWidth())
        self.downlink_icon.setSizePolicy(sizePolicy)
        self.downlink_icon.setMinimumSize(QtCore.QSize(25, 25))
        self.downlink_icon.setMaximumSize(QtCore.QSize(25, 25))
        self.downlink_icon.setText(_fromUtf8(""))
        self.downlink_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/downlink-green/img/downlink-color-green.png")))
        self.downlink_icon.setScaledContents(True)
        self.downlink_icon.setWordWrap(False)
        self.downlink_icon.setObjectName(_fromUtf8("downlink_icon"))
        self.gridLayout.addWidget(self.downlink_icon, 0, 0, 1, 1)
        self.upload_status_icon = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_status_icon.sizePolicy().hasHeightForWidth())
        self.upload_status_icon.setSizePolicy(sizePolicy)
        self.upload_status_icon.setMinimumSize(QtCore.QSize(25, 25))
        self.upload_status_icon.setMaximumSize(QtCore.QSize(25, 25))
        self.upload_status_icon.setText(_fromUtf8(""))
        self.upload_status_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/cloud-online/img/cloud-online.svg")))
        self.upload_status_icon.setScaledContents(True)
        self.upload_status_icon.setObjectName(_fromUtf8("upload_status_icon"))
        self.gridLayout.addWidget(self.upload_status_icon, 0, 4, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 2, 1, 1)
        self.label_uuid_value = QtGui.QLabel(self.gridLayoutWidget)
        self.label_uuid_value.setMinimumSize(QtCore.QSize(0, 25))
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
        self.gridLayout_5.addWidget(self.label_uuid_value, 0, 1, 1, 1)
        self.label_uuid_text = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_uuid_text.setFont(font)
        self.label_uuid_text.setObjectName(_fromUtf8("label_uuid_text"))
        self.gridLayout_5.addWidget(self.label_uuid_text, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_timestamp = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_timestamp.sizePolicy().hasHeightForWidth())
        self.label_timestamp.setSizePolicy(sizePolicy)
        self.label_timestamp.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_timestamp.setFont(font)
        self.label_timestamp.setObjectName(_fromUtf8("label_timestamp"))
        self.gridLayout_4.addWidget(self.label_timestamp, 0, 0, 1, 1)
        self.label_frame_type = QtGui.QPushButton(self.gridLayoutWidget)
        self.label_frame_type.setMinimumSize(QtCore.QSize(0, 20))
        self.label_frame_type.setAutoFillBackground(False)
        self.label_frame_type.setObjectName(_fromUtf8("label_frame_type"))
        self.gridLayout_4.addWidget(self.label_frame_type, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.downlink_icon.setToolTip(_translate("Form", "Downlink", None))
        self.upload_status_icon.setToolTip(_translate("Form", "Frame successfully sent to server, thanks!", None))
        self.label_uuid_value.setToolTip(_translate("Form", "Click to see the frame content", None))
        self.label_uuid_value.setText(_translate("Form", "14016296-8d4f-4a25-8911-5ecaeb13d9ffp", None))
        self.label_uuid_text.setText(_translate("Form", "uuid: ", None))
        self.label_timestamp.setToolTip(_translate("Form", "Timestamp", None))
        self.label_timestamp.setText(_translate("Form", "2017-11-30 11:14:33", None))
        self.label_frame_type.setText(_translate("Form", "PushButton", None))

import img_pix_rc

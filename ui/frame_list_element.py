# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\frame_list_element.ui'
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

class UiFrameListWidget(QtGui.QWidget):
    def __init__ (self, parent=None):
        super(QtGui.QWidget, self).__init__(parent)
        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -2, 501, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.downlinkIconLabel = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downlinkIconLabel.sizePolicy().hasHeightForWidth())
        self.downlinkIconLabel.setSizePolicy(sizePolicy)
        self.downlinkIconLabel.setMinimumSize(QtCore.QSize(25, 25))
        self.downlinkIconLabel.setMaximumSize(QtCore.QSize(25, 25))
        self.downlinkIconLabel.setText(_fromUtf8(""))
        self.downlinkIconLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/downlink-green/img/downlink-color-green.png")))
        self.downlinkIconLabel.setScaledContents(True)
        self.downlinkIconLabel.setWordWrap(False)
        self.downlinkIconLabel.setObjectName(_fromUtf8("downlinkIconLabel"))
        self.horizontalLayout.addWidget(self.downlinkIconLabel)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.uuidTextLabel = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uuidTextLabel.setFont(font)
        self.uuidTextLabel.setStyleSheet(_fromUtf8("font-size: 16px;"))
        self.uuidTextLabel.setObjectName(_fromUtf8("uuidTextLabel"))
        self.gridLayout_5.addWidget(self.uuidTextLabel, 0, 0, 1, 1)
        self.uuidValueLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.uuidValueLabel.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uuidValueLabel.setFont(font)
        self.uuidValueLabel.setStyleSheet(_fromUtf8("font-size: 16px;"))
        self.uuidValueLabel.setScaledContents(False)
        self.uuidValueLabel.setWordWrap(False)
        self.uuidValueLabel.setOpenExternalLinks(True)
        self.uuidValueLabel.setObjectName(_fromUtf8("uuidValueLabel"))
        self.gridLayout_5.addWidget(self.uuidValueLabel, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frameTypeLabel = QtGui.QPushButton(self.gridLayoutWidget)
        self.frameTypeLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.frameTypeLabel.setAutoFillBackground(False)
        self.frameTypeLabel.setObjectName(_fromUtf8("frameTypeLabel"))
        self.gridLayout_4.addWidget(self.frameTypeLabel, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 1, 1, 1)
        self.timestampLabel = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.timestampLabel.sizePolicy().hasHeightForWidth())
        self.timestampLabel.setSizePolicy(sizePolicy)
        self.timestampLabel.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timestampLabel.setFont(font)
        self.timestampLabel.setStyleSheet(_fromUtf8("font-size: 16px;"))
        self.timestampLabel.setObjectName(_fromUtf8("timestampLabel"))
        self.gridLayout_4.addWidget(self.timestampLabel, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.uploadStatusIconButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.uploadStatusIconButton.setMinimumSize(QtCore.QSize(25, 25))
        self.uploadStatusIconButton.setMaximumSize(QtCore.QSize(25, 25))
        self.uploadStatusIconButton.setStyleSheet(_fromUtf8("QPushButton:pressed { border-style: none;}"))
        self.uploadStatusIconButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/cloud-online/img/cloud-online.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadStatusIconButton.setIcon(icon)
        self.uploadStatusIconButton.setIconSize(QtCore.QSize(25, 25))
        self.uploadStatusIconButton.setDefault(False)
        self.uploadStatusIconButton.setFlat(True)
        self.uploadStatusIconButton.setObjectName(_fromUtf8("uploadStatusIconButton"))
        self.horizontalLayout.addWidget(self.uploadStatusIconButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.downlinkIconLabel.setToolTip(_translate("Form", "Downlink", None))
        self.uuidTextLabel.setToolTip(_translate("Form", "Frame identifier on server", None))
        self.uuidTextLabel.setText(_translate("Form", "uuid:", None))
        self.uuidValueLabel.setToolTip(_translate("Form", "Click to see the frame content", None))
        self.uuidValueLabel.setText(_translate("Form", "Frame not send to cloud yet", None))
        self.frameTypeLabel.setText(_translate("Form", "PushButton", None))
        self.timestampLabel.setToolTip(_translate("Form", "Timestamp", None))
        self.timestampLabel.setText(_translate("Form", "2017-11-30 11:14:33", None))

import img_pix_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(660, 605)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(660, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/pw-sat2-logo/img/pw-sat2-logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.ribbon = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ribbon.sizePolicy().hasHeightForWidth())
        self.ribbon.setSizePolicy(sizePolicy)
        self.ribbon.setMinimumSize(QtCore.QSize(0, 105))
        self.ribbon.setMaximumSize(QtCore.QSize(16777215, 105))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ribbon.setFont(font)
        self.ribbon.setToolTip(_fromUtf8(""))
        self.ribbon.setStyleSheet(_fromUtf8("QTabBar::tab { height: 35px;}"))
        self.ribbon.setIconSize(QtCore.QSize(20, 20))
        self.ribbon.setElideMode(QtCore.Qt.ElideNone)
        self.ribbon.setDocumentMode(False)
        self.ribbon.setTabsClosable(False)
        self.ribbon.setMovable(False)
        self.ribbon.setObjectName(_fromUtf8("ribbon"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 631, 64))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.helpAccountButton = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpAccountButton.sizePolicy().hasHeightForWidth())
        self.helpAccountButton.setSizePolicy(sizePolicy)
        self.helpAccountButton.setMinimumSize(QtCore.QSize(50, 50))
        self.helpAccountButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/help/img/question-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpAccountButton.setIcon(icon1)
        self.helpAccountButton.setIconSize(QtCore.QSize(35, 35))
        self.helpAccountButton.setObjectName(_fromUtf8("helpAccountButton"))
        self.gridLayout_2.addWidget(self.helpAccountButton, 0, 8, 1, 1)
        self.credentialsLoadButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.credentialsLoadButton.setMinimumSize(QtCore.QSize(0, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/credentials/img/key-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.credentialsLoadButton.setIcon(icon2)
        self.credentialsLoadButton.setIconSize(QtCore.QSize(35, 35))
        self.credentialsLoadButton.setObjectName(_fromUtf8("credentialsLoadButton"))
        self.gridLayout_2.addWidget(self.credentialsLoadButton, 0, 2, 1, 1)
        self.credentialsButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.credentialsButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credentialsButton.sizePolicy().hasHeightForWidth())
        self.credentialsButton.setSizePolicy(sizePolicy)
        self.credentialsButton.setMinimumSize(QtCore.QSize(0, 50))
        self.credentialsButton.setMaximumSize(QtCore.QSize(250, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/user/img/user-alt-slash-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.credentialsButton.setIcon(icon3)
        self.credentialsButton.setIconSize(QtCore.QSize(35, 35))
        self.credentialsButton.setObjectName(_fromUtf8("credentialsButton"))
        self.gridLayout_2.addWidget(self.credentialsButton, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.line_2 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_2.setMinimumSize(QtCore.QSize(10, 50))
        self.line_2.setMaximumSize(QtCore.QSize(10, 50))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 0, 7, 1, 1)
        self.ribbon.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.tab_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 631, 61))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.helpSignalSourceButton = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpSignalSourceButton.sizePolicy().hasHeightForWidth())
        self.helpSignalSourceButton.setSizePolicy(sizePolicy)
        self.helpSignalSourceButton.setMinimumSize(QtCore.QSize(50, 50))
        self.helpSignalSourceButton.setText(_fromUtf8(""))
        self.helpSignalSourceButton.setIcon(icon1)
        self.helpSignalSourceButton.setIconSize(QtCore.QSize(35, 35))
        self.helpSignalSourceButton.setObjectName(_fromUtf8("helpSignalSourceButton"))
        self.gridLayout_5.addWidget(self.helpSignalSourceButton, 0, 4, 1, 1)
        self.signalSourceDropdownButton = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.signalSourceDropdownButton.setMinimumSize(QtCore.QSize(100, 50))
        self.signalSourceDropdownButton.setObjectName(_fromUtf8("signalSourceDropdownButton"))
        self.signalSourceDropdownButton.addItem(_fromUtf8(""))
        self.signalSourceDropdownButton.addItem(_fromUtf8(""))
        self.signalSourceDropdownButton.addItem(_fromUtf8(""))
        self.signalSourceDropdownButton.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.signalSourceDropdownButton, 0, 0, 1, 1)
        self.runSourceButton = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.runSourceButton.setMinimumSize(QtCore.QSize(50, 50))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/source/img/play-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runSourceButton.setIcon(icon4)
        self.runSourceButton.setIconSize(QtCore.QSize(35, 35))
        self.runSourceButton.setObjectName(_fromUtf8("runSourceButton"))
        self.gridLayout_5.addWidget(self.runSourceButton, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 1, 1, 1)
        self.ribbon.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.tab_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 631, 61))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.runDemodulatorButton = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.runDemodulatorButton.setMinimumSize(QtCore.QSize(50, 50))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/demodulator/img/signature-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runDemodulatorButton.setIcon(icon5)
        self.runDemodulatorButton.setIconSize(QtCore.QSize(35, 35))
        self.runDemodulatorButton.setObjectName(_fromUtf8("runDemodulatorButton"))
        self.gridLayout_6.addWidget(self.runDemodulatorButton, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 1, 1, 1)
        self.helpDemodulatorButton = QtGui.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpDemodulatorButton.sizePolicy().hasHeightForWidth())
        self.helpDemodulatorButton.setSizePolicy(sizePolicy)
        self.helpDemodulatorButton.setMinimumSize(QtCore.QSize(50, 50))
        self.helpDemodulatorButton.setText(_fromUtf8(""))
        self.helpDemodulatorButton.setIcon(icon1)
        self.helpDemodulatorButton.setIconSize(QtCore.QSize(35, 35))
        self.helpDemodulatorButton.setObjectName(_fromUtf8("helpDemodulatorButton"))
        self.gridLayout_6.addWidget(self.helpDemodulatorButton, 0, 2, 1, 1)
        self.ribbon.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.tab_5)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 631, 61))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_7 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 0, 5, 1, 1)
        self.helpCloudUploadButton = QtGui.QPushButton(self.gridLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpCloudUploadButton.sizePolicy().hasHeightForWidth())
        self.helpCloudUploadButton.setSizePolicy(sizePolicy)
        self.helpCloudUploadButton.setMinimumSize(QtCore.QSize(50, 50))
        self.helpCloudUploadButton.setText(_fromUtf8(""))
        self.helpCloudUploadButton.setIcon(icon1)
        self.helpCloudUploadButton.setIconSize(QtCore.QSize(35, 35))
        self.helpCloudUploadButton.setObjectName(_fromUtf8("helpCloudUploadButton"))
        self.gridLayout_7.addWidget(self.helpCloudUploadButton, 0, 6, 1, 1)
        self.autoUploadToolButton = QtGui.QToolButton(self.gridLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoUploadToolButton.sizePolicy().hasHeightForWidth())
        self.autoUploadToolButton.setSizePolicy(sizePolicy)
        self.autoUploadToolButton.setMinimumSize(QtCore.QSize(55, 50))
        self.autoUploadToolButton.setBaseSize(QtCore.QSize(0, 0))
        self.autoUploadToolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.autoUploadToolButton.setAutoFillBackground(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/auto-upload-offline/img/cloud-upload-alt-solid-disabled.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/cloud-upload/img/cloud-upload-alt-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/cloud-upload/img/cloud-upload-alt-solid.svg")), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/cloud-upload/img/cloud-upload-alt-solid.svg")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/cloud-upload/img/cloud-upload-alt-solid.svg")), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.autoUploadToolButton.setIcon(icon6)
        self.autoUploadToolButton.setIconSize(QtCore.QSize(35, 35))
        self.autoUploadToolButton.setCheckable(True)
        self.autoUploadToolButton.setChecked(True)
        self.autoUploadToolButton.setAutoRepeat(True)
        self.autoUploadToolButton.setAutoExclusive(False)
        self.autoUploadToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.autoUploadToolButton.setObjectName(_fromUtf8("autoUploadToolButton"))
        self.gridLayout_7.addWidget(self.autoUploadToolButton, 0, 2, 1, 1)
        self.loadFramesFromFileButton = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.loadFramesFromFileButton.setMinimumSize(QtCore.QSize(0, 50))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/load-frames/img/file-import-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadFramesFromFileButton.setIcon(icon7)
        self.loadFramesFromFileButton.setIconSize(QtCore.QSize(35, 35))
        self.loadFramesFromFileButton.setObjectName(_fromUtf8("loadFramesFromFileButton"))
        self.gridLayout_7.addWidget(self.loadFramesFromFileButton, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.gridLayoutWidget_5)
        self.line.setMinimumSize(QtCore.QSize(10, 50))
        self.line.setMaximumSize(QtCore.QSize(10, 50))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_7.addWidget(self.line, 0, 1, 1, 1)
        self.sendUnsuccessfulButton = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.sendUnsuccessfulButton.setMinimumSize(QtCore.QSize(0, 50))
        self.sendUnsuccessfulButton.setToolTip(_fromUtf8("Click to try again sending frames that have not been successfully sent (labeled with error)."))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/cloud-upload/img/cloud-upload-alt-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendUnsuccessfulButton.setIcon(icon8)
        self.sendUnsuccessfulButton.setIconSize(QtCore.QSize(35, 35))
        self.sendUnsuccessfulButton.setObjectName(_fromUtf8("sendUnsuccessfulButton"))
        self.gridLayout_7.addWidget(self.sendUnsuccessfulButton, 0, 4, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem6, 0, 3, 1, 1)
        self.ribbon.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.ribbon)
        self.framesListWidget = QtGui.QListWidget(self.centralwidget)
        self.framesListWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framesListWidget.sizePolicy().hasHeightForWidth())
        self.framesListWidget.setSizePolicy(sizePolicy)
        self.framesListWidget.setMinimumSize(QtCore.QSize(520, 65))
        self.framesListWidget.setMaximumSize(QtCore.QSize(2000, 10000))
        self.framesListWidget.setBaseSize(QtCore.QSize(0, 0))
        self.framesListWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.framesListWidget.setResizeMode(QtGui.QListView.Adjust)
        self.framesListWidget.setObjectName(_fromUtf8("framesListWidget"))
        self.verticalLayout_3.addWidget(self.framesListWidget)
        spacerItem7 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem7)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.ribbon.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "PW-Sat2 Ground Station - Main Window", None))
        self.helpAccountButton.setToolTip(_translate("mainWindow", "Help on Account", None))
        self.credentialsLoadButton.setToolTip(_translate("mainWindow", "Click the button to load new credentials...", None))
        self.credentialsLoadButton.setText(_translate("mainWindow", "Load credentials from file", None))
        self.credentialsButton.setToolTip(_translate("mainWindow", "Account info", None))
        self.credentialsButton.setText(_translate("mainWindow", "ham-mail@pw-sat.pl", None))
        self.ribbon.setTabText(self.ribbon.indexOf(self.tab), _translate("mainWindow", "Account", None))
        self.helpSignalSourceButton.setToolTip(_translate("mainWindow", "Help on Signal Source", None))
        self.signalSourceDropdownButton.setItemText(0, _translate("mainWindow", "Recorded IQ File", None))
        self.signalSourceDropdownButton.setItemText(1, _translate("mainWindow", "FUNcube Dongle Pro+", None))
        self.signalSourceDropdownButton.setItemText(2, _translate("mainWindow", "RTL-SDR", None))
        self.signalSourceDropdownButton.setItemText(3, _translate("mainWindow", "PlutoSDR", None))
        self.runSourceButton.setText(_translate("mainWindow", "Run source", None))
        self.ribbon.setTabText(self.ribbon.indexOf(self.tab_3), _translate("mainWindow", "Signal Source", None))
        self.runDemodulatorButton.setToolTip(_translate("mainWindow", "Run Demodulator", None))
        self.runDemodulatorButton.setText(_translate("mainWindow", "Run Demodulator", None))
        self.helpDemodulatorButton.setToolTip(_translate("mainWindow", "Help on Demodulator", None))
        self.ribbon.setTabText(self.ribbon.indexOf(self.tab_4), _translate("mainWindow", "Demodulator", None))
        self.helpCloudUploadButton.setToolTip(_translate("mainWindow", "Help on Cloud Upload", None))
        self.autoUploadToolButton.setToolTip(_translate("mainWindow", "Send frames from the list to cloud", None))
        self.autoUploadToolButton.setText(_translate("mainWindow", "Auto-Upload Enabled", None))
        self.loadFramesFromFileButton.setToolTip(_translate("mainWindow", "Upload frames saved in *.frames file", None))
        self.loadFramesFromFileButton.setText(_translate("mainWindow", "Load From File", None))
        self.sendUnsuccessfulButton.setText(_translate("mainWindow", "Re-Upload Failed", None))
        self.ribbon.setTabText(self.ribbon.indexOf(self.tab_5), _translate("mainWindow", "Cloud Upload", None))
        self.framesListWidget.setSortingEnabled(False)

import img_pix_rc

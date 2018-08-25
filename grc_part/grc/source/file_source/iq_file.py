# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\iq_file.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(584, 201)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(584, 190))
        MainWindow.setMaximumSize(QtCore.QSize(584, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/img/pw-sat2-logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 581, 201))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self._2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self._2.setObjectName(_fromUtf8("_2"))
        spacerItem = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self._2.addItem(spacerItem, 1, 1, 1, 1)
        self.appStatusLabel = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.appStatusLabel.setFont(font)
        self.appStatusLabel.setObjectName(_fromUtf8("appStatusLabel"))
        self._2.addWidget(self.appStatusLabel, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonPlay = QtGui.QPushButton(self.gridLayoutWidget)
        self.buttonPlay.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.buttonPlay.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/img/play-circle-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(icon1)
        self.buttonPlay.setIconSize(QtCore.QSize(25, 25))
        self.buttonPlay.setObjectName(_fromUtf8("buttonPlay"))
        self.horizontalLayout.addWidget(self.buttonPlay)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.statusLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.statusLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout.addWidget(self.statusLabel)
        self._2.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self._2.addItem(spacerItem4, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pathInput = QtGui.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathInput.sizePolicy().hasHeightForWidth())
        self.pathInput.setSizePolicy(sizePolicy)
        self.pathInput.setMinimumSize(QtCore.QSize(400, 30))
        self.pathInput.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pathInput.setObjectName(_fromUtf8("pathInput"))
        self.horizontalLayout_2.addWidget(self.pathInput)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.buttonChoose = QtGui.QPushButton(self.gridLayoutWidget)
        self.buttonChoose.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonChoose.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/img/folder-open-solid.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonChoose.setIcon(icon2)
        self.buttonChoose.setIconSize(QtCore.QSize(25, 25))
        self.buttonChoose.setObjectName(_fromUtf8("buttonChoose"))
        self.horizontalLayout_2.addWidget(self.buttonChoose)
        self._2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem6, 2, 2, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setMinimumSize(QtCore.QSize(100, 5))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self._2.addWidget(self.progressBar, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "IQ File Source", None))
        self.appStatusLabel.setText(_translate("MainWindow", "Choose IQ file path and click Play button", None))
        self.buttonPlay.setText(_translate("MainWindow", "Play", None))
        self.statusLabel.setText(_translate("MainWindow", "Idle", None))
        self.buttonChoose.setText(_translate("MainWindow", "Browse", None))

import icons_rc

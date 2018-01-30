# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 130, 1401, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pathLabel.setFont(font)
        self.pathLabel.setObjectName("pathLabel")
        self.horizontalLayout.addWidget(self.pathLabel)
        self.pathText = QtWidgets.QTextEdit(self.layoutWidget)
        self.pathText.setObjectName("pathText")
        self.horizontalLayout.addWidget(self.pathText)
        self.pathBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.pathBtn.setObjectName("pathBtn")
        self.horizontalLayout.addWidget(self.pathBtn)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 50, 821, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_2.addWidget(self.nameLabel)
        self.nameText = QtWidgets.QTextEdit(self.layoutWidget1)
        self.nameText.setObjectName("nameText")
        self.horizontalLayout_2.addWidget(self.nameText)
        self.graphicsView = GraphicsLayoutWidget(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(60, 230, 1801, 611))
        self.graphicsView.setObjectName("graphicsView")
        self.startBtn = QtWidgets.QPushButton(self.centralWidget)
        self.startBtn.setGeometry(QtCore.QRect(140, 880, 601, 91))
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralWidget)
        self.stopBtn.setGeometry(QtCore.QRect(1100, 880, 601, 91))
        self.stopBtn.setObjectName("stopBtn")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 37))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pathLabel.setText(_translate("MainWindow", "Save Path : "))
        self.pathBtn.setText(_translate("MainWindow", "..."))
        self.nameLabel.setText(_translate("MainWindow", "File name : "))
        self.nameText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">test</p></body></html>"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))

from pyqtgraph import GraphicsLayoutWidget

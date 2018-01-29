# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verifywindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_verifyWindow(object):
    def setupUi(self, verifyWindow):
        verifyWindow.setObjectName("verifyWindow")
        verifyWindow.resize(1080, 800)
        self.centralWidget = QtWidgets.QWidget(verifyWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.infoText = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.infoText.setGeometry(QtCore.QRect(40, 160, 991, 551))
        self.infoText.setObjectName("infoText")
        self.inputWavLabel = QtWidgets.QLabel(self.centralWidget)
        self.inputWavLabel.setGeometry(QtCore.QRect(40, 40, 181, 32))
        self.inputWavLabel.setObjectName("inputWavLabel")
        self.inputWavText = QtWidgets.QTextEdit(self.centralWidget)
        self.inputWavText.setGeometry(QtCore.QRect(220, 30, 201, 51))
        self.inputWavText.setObjectName("inputWavText")
        self.infoLabel = QtWidgets.QLabel(self.centralWidget)
        self.infoLabel.setGeometry(QtCore.QRect(40, 110, 361, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName("infoLabel")
        verifyWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(verifyWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1080, 37))
        self.menuBar.setObjectName("menuBar")
        verifyWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(verifyWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        verifyWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(verifyWindow)
        self.statusBar.setObjectName("statusBar")
        verifyWindow.setStatusBar(self.statusBar)

        self.retranslateUi(verifyWindow)
        QtCore.QMetaObject.connectSlotsByName(verifyWindow)

    def retranslateUi(self, verifyWindow):
        _translate = QtCore.QCoreApplication.translate
        verifyWindow.setWindowTitle(_translate("verifyWindow", "verifyWindow"))
        self.inputWavLabel.setText(_translate("verifyWindow", "Input Wav :"))
        self.inputWavText.setHtml(_translate("verifyWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">test.wav</p></body></html>"))
        self.infoLabel.setText(_translate("verifyWindow", "Output Information :"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui',
# licensing of 'MainUi.ui' applies.
#
# Created: Sat Oct 19 19:21:29 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 470, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(23, 130, 761, 331))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 60, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(340, 500, 113, 32))
        self.clear.setObjectName("clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.pushButton.clicked.connect(self.printDennts)
        #self.clear.clicked.connect(self.cleartext)
        #self.pushButton.clicked.connect(self.printMessage)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.clear.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))

    #def printMessage(self):
        #print ("Hello World")

    #def printDennts(self):
        #self.textEdit.setText(self.lineEdit.text()+ " Dennts")

    #def cleartext(self):
        #self.textEdit.setText("")



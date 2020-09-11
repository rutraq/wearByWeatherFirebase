# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 415)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxShop = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxShop.setGeometry(QtCore.QRect(760, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxShop.setFont(font)
        self.comboBoxShop.setCurrentText("")
        self.comboBoxShop.setObjectName("comboBoxShop")
        self.comboBoxItem = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxItem.setGeometry(QtCore.QRect(60, 50, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxItem.setFont(font)
        self.comboBoxItem.setCurrentText("")
        self.comboBoxItem.setObjectName("comboBoxItem")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 111, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEditPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPath.setGeometry(QtCore.QRect(290, 50, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEditPath.setFont(font)
        self.lineEditPath.setObjectName("lineEditPath")
        self.lineEditUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUrl.setGeometry(QtCore.QRect(500, 50, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEditUrl.setFont(font)
        self.lineEditUrl.setObjectName("lineEditUrl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ссылка на одежду"))
        self.label_2.setText(_translate("MainWindow", "Путь к одежде"))
        self.pushButton.setText(_translate("MainWindow", "Add item"))



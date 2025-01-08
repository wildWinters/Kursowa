# -*- coding: cp1251 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_T_Fwindow(object):
    def setupUi(self, T_Fwindow):
        T_Fwindow.setObjectName("T_Fwindow")
        T_Fwindow.setEnabled(True)
        T_Fwindow.resize(920, 795)
        T_Fwindow.setStyleSheet("background-color: #808080")
        self.T_Fwidget = QtWidgets.QWidget(T_Fwindow)
        self.T_Fwidget.setObjectName("T_Fwidget")
        self.NextButton = QtWidgets.QPushButton(self.T_Fwidget)
        self.NextButton.setGeometry(QtCore.QRect(480, 560, 300, 150))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.NextButton.setFont(font)
        self.NextButton.setStyleSheet("QPushButton{\n"
"    background-color: #808080;    \n"
"    border-radius:10;\n"
"color: #00008B;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#00bfff;\n"
"}")
        self.NextButton.setObjectName("NextButton")
        self.Tline = QtWidgets.QLineEdit(self.T_Fwidget)
        self.Tline.setGeometry(QtCore.QRect(30, 250, 851, 231))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.Tline.setFont(font)
        self.Tline.setStyleSheet("background-color:#4682B4;\n"
"border-radius: 10;\n"
"border: 5px solid #40E0D0")
        self.Tline.setText("")
        self.Tline.setAlignment(QtCore.Qt.AlignCenter)
        self.Tline.setReadOnly(True)
        self.Tline.setObjectName("Tline")
        self.EndButton = QtWidgets.QPushButton(self.T_Fwidget)
        self.EndButton.setGeometry(QtCore.QRect(120, 560, 300, 150))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.EndButton.setFont(font)
        self.EndButton.setStyleSheet("QPushButton{\n"
"    background-color: #808080;    \n"
"    border-radius:10;\n"
"color: #8B0000;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#00bfff;\n"
"}")
        self.EndButton.setObjectName("EndButton")
        self.T_Fline = QtWidgets.QLineEdit(self.T_Fwidget)
        self.T_Fline.setGeometry(QtCore.QRect(30, 30, 851, 231))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.T_Fline.setFont(font)
        self.T_Fline.setStyleSheet("background-color:#4682B4;\n"
"border-radius: 10;\n"
"border: 5px solid #40E0D0")
        self.T_Fline.setText("")
        self.T_Fline.setAlignment(QtCore.Qt.AlignCenter)
        self.T_Fline.setReadOnly(True)
        self.T_Fline.setObjectName("T_Fline")
        T_Fwindow.setCentralWidget(self.T_Fwidget)

        self.retranslateUi(T_Fwindow)
        QtCore.QMetaObject.connectSlotsByName(T_Fwindow)

    def retranslateUi(self, T_Fwindow):
        _translate = QtCore.QCoreApplication.translate
        T_Fwindow.setWindowTitle(_translate("T_Fwindow", "MainWindow"))
        self.NextButton.setText(_translate("T_Fwindow", "Continue\n\t\b  "
"testing"))
        self.EndButton.setText(_translate("T_Fwindow", "click to end \n\t\b "
"testing"))



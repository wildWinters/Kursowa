# -*- coding: cp1251 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestResultWindow(object):

	def setupUi(self, TestResultWindow):
		TestResultWindow.setObjectName("TestResultWindow")
		TestResultWindow.resize(920, 795)
		TestResultWindow.setStyleSheet("background-color:#808080\n"
"")
		self.TestResultWidget = QtWidgets.QWidget(TestResultWindow)
		self.TestResultWidget.setObjectName("TestResultWidget")
		self.HomeButton = QtWidgets.QPushButton(self.TestResultWidget)
		self.HomeButton.setGeometry(QtCore.QRect(130, 580, 661, 161))
		font = QtGui.QFont()
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)
		self.HomeButton.setFont(font)
		self.HomeButton.setStyleSheet("QPushButton{\n"
"   color: black;\n"
"   background-color: blue;\n"
"    border-radius: 10;\n"
"}\n"
"QPushButton:pressed{\n"
"   background-color:#00bfff;\n"
"}")
		self.HomeButton.setObjectName("HomeButton")
		self.frame = QtWidgets.QFrame(self.TestResultWidget)
		self.frame.setGeometry(QtCore.QRect(40, 50, 811, 461))
		self.frame.setStyleSheet("background-color:#cccc00;\n"
"border-radius: 10;\n"
"border: 5px solid purple;\n"
"\n"
"")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.label_3 = QtWidgets.QLabel(self.frame)
		self.label_3.setGeometry(QtCore.QRect(80, 190, 541, 101))
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setStyleSheet("border: 0px\n"
"")
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.frame)
		self.label_4.setGeometry(QtCore.QRect(80, 320, 461, 101))
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setStyleSheet("border:0px")
		self.label_4.setObjectName("label_4")
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(80, 40, 471, 121))
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setStyleSheet("border: 0px")
		self.label.setObjectName("label")
		self.QuanQuest = QtWidgets.QLineEdit(self.frame)
		self.QuanQuest.setGeometry(QtCore.QRect(610, 50, 141, 101))
		font = QtGui.QFont()
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)
		self.QuanQuest.setFont(font)
		self.QuanQuest.setStyleSheet("border: 10px solid red")
		self.QuanQuest.setText("")
		self.QuanQuest.setReadOnly(True)
		self.QuanQuest.setObjectName("QuanQuest")
		self.TrueAnsw = QtWidgets.QLineEdit(self.frame)
		self.TrueAnsw.setGeometry(QtCore.QRect(610, 190, 141, 101))
		font = QtGui.QFont()
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)
		self.TrueAnsw.setFont(font)
		self.TrueAnsw.setStyleSheet("border: 10px solid  red")
		self.TrueAnsw.setText("")
		self.TrueAnsw.setReadOnly(True)
		self.TrueAnsw.setObjectName("TrueAnsw")
		self.TimeMin = QtWidgets.QLineEdit(self.frame)
		self.TimeMin.setGeometry(QtCore.QRect(550, 320, 201, 101))
		font = QtGui.QFont()
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)
		self.TimeMin.setFont(font)
		self.TimeMin.setStyleSheet("border: 10px solid  red")
		self.TimeMin.setText("")
		self.TimeMin.setReadOnly(True)
		self.TimeMin.setObjectName("TimeMin")
		TestResultWindow.setCentralWidget(self.TestResultWidget)

		self.retranslateUi(TestResultWindow)
		QtCore.QMetaObject.connectSlotsByName(TestResultWindow)

	def retranslateUi(self, TestResultWindow):
		_translate = QtCore.QCoreApplication.translate
		TestResultWindow.setWindowTitle(_translate("TestResultWindow", "MainWindow"))
		self.HomeButton.setText(_translate("TestResultWindow", "Main Menu"))
		self.label_3.setText(_translate("TestResultWindow", "Number of correct answers"))
		self.label_4.setText(_translate("TestResultWindow", "Test completion time (min)"))
		self.label.setText(_translate("TestResultWindow", "Number of completed questions"))

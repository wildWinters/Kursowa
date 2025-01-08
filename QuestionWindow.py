# -*- coding: cp1251 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Task(object):

	def setupUi(self, Task):
		Task.setObjectName("Task")
		Task.setEnabled(True)
		Task.resize(920, 795)
		self.TaskWidget = QtWidgets.QWidget(Task)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(50)
		sizePolicy.setVerticalStretch(50)
		sizePolicy.setHeightForWidth(self.TaskWidget.sizePolicy().hasHeightForWidth())
		self.TaskWidget.setSizePolicy(sizePolicy)
		self.TaskWidget.setStyleSheet("background-color: #808080\n"
"")
		self.TaskWidget.setObjectName("TaskWidget")
		self.AnswerButton = QtWidgets.QPushButton(self.TaskWidget)
		self.AnswerButton.setGeometry(QtCore.QRect(320, 550, 250, 120))
		font = QtGui.QFont()
		font.setFamily("Rockwell Extra Bold")
		font.setPointSize(24)
		font.setBold(True)
		font.setWeight(75)
		self.AnswerButton.setFont(font)
		self.AnswerButton.setStyleSheet("QPushButton{\n"
"    background-color: blue;\n"
"    border-radius:10;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#00bfff;\n"
"}")
		self.AnswerButton.setObjectName("AnswerButton")
		self.AnswerLine = QtWidgets.QLineEdit(self.TaskWidget)
		self.AnswerLine.setGeometry(QtCore.QRect(290, 380, 311, 141))
		font = QtGui.QFont()
		font.setFamily("Rockwell Extra Bold")
		font.setPointSize(60)
		font.setBold(True)
		font.setWeight(75)
		self.AnswerLine.setFont(font)
		self.AnswerLine.setStyleSheet("background-color: #cccc00;\n"
"border-radius: 10;\n"
"border: 5px solid red    ;")
		self.AnswerLine.setAlignment(QtCore.Qt.AlignCenter)
		self.AnswerLine.setObjectName("AnswerLine")
		self.NumberLine = QtWidgets.QLineEdit(self.TaskWidget)
		self.NumberLine.setGeometry(QtCore.QRect(10, 10, 431, 111))
		font = QtGui.QFont()
		font.setFamily("Rockwell Extra Bold")
		font.setPointSize(24)
		font.setBold(True)
		font.setWeight(75)
		self.NumberLine.setFont(font)
		self.NumberLine.setStyleSheet("background-color:#FF1493;\n"
"border: 5px solid grey    ;\n"
"border-radius: 10")
		self.NumberLine.setAlignment(QtCore.Qt.AlignCenter)
		self.NumberLine.setReadOnly(True)
		self.NumberLine.setObjectName("NumberLine")
		self.QuestionLine = QtWidgets.QLineEdit(self.TaskWidget)
		self.QuestionLine.setGeometry(QtCore.QRect(150, 129, 611, 231))
		font = QtGui.QFont()
		font.setFamily("Tw Cen MT Condensed Extra Bold")
		font.setPointSize(150)
		self.QuestionLine.setFont(font)
		self.QuestionLine.setStyleSheet("background-color:#4682B4;\n"
"border-radius: 10;\n"
"border: 5px solid #40E0D0    ;")
		self.QuestionLine.setAlignment(QtCore.Qt.AlignCenter)
		self.QuestionLine.setReadOnly(True)
		self.QuestionLine.setObjectName("QuestionLine")
		Task.setCentralWidget(self.TaskWidget)

		self.retranslateUi(Task)
		QtCore.QMetaObject.connectSlotsByName(Task)

	def retranslateUi(self, Task):
		_translate = QtCore.QCoreApplication.translate
		Task.setWindowTitle(_translate("Task", "MainWindow "))
		self.AnswerButton.setText(_translate("Task", "Answer  "))

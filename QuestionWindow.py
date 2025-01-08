# # -*- coding: cp1251 -*-

# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_Task(object):

# 	def setupUi(self, Task):
# 		Task.setObjectName("Task")
# 		Task.setEnabled(True)
# 		Task.resize(920, 795)
# 		self.TaskWidget = QtWidgets.QWidget(Task)
# 		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
# 		sizePolicy.setHorizontalStretch(50)
# 		sizePolicy.setVerticalStretch(50)
# 		sizePolicy.setHeightForWidth(self.TaskWidget.sizePolicy().hasHeightForWidth())
# 		self.TaskWidget.setSizePolicy(sizePolicy)
# 		self.TaskWidget.setStyleSheet("background-color: #808080\n"
# "")
# 		self.TaskWidget.setObjectName("TaskWidget")
# 		self.AnswerButton = QtWidgets.QPushButton(self.TaskWidget)
# 		self.AnswerButton.setGeometry(QtCore.QRect(320, 550, 250, 120))
# 		font = QtGui.QFont()
# 		font.setFamily("Rockwell Extra Bold")
# 		font.setPointSize(24)
# 		font.setBold(True)
# 		font.setWeight(75)
# 		self.AnswerButton.setFont(font)
# 		self.AnswerButton.setStyleSheet("QPushButton{\n"
# "    background-color: blue;\n"
# "    border-radius:10;\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color:#00bfff;\n"
# "}")
# 		self.AnswerButton.setObjectName("AnswerButton")
# 		self.AnswerLine = QtWidgets.QLineEdit(self.TaskWidget)
# 		self.AnswerLine.setGeometry(QtCore.QRect(290, 380, 311, 141))
# 		font = QtGui.QFont()
# 		font.setFamily("Rockwell Extra Bold")
# 		font.setPointSize(60)
# 		font.setBold(True)
# 		font.setWeight(75)
# 		self.AnswerLine.setFont(font)
# 		self.AnswerLine.setStyleSheet("background-color: #cccc00;\n"
# "border-radius: 10;\n"
# "border: 5px solid red    ;")
# 		self.AnswerLine.setAlignment(QtCore.Qt.AlignCenter)
# 		self.AnswerLine.setObjectName("AnswerLine")
# 		self.NumberLine = QtWidgets.QLineEdit(self.TaskWidget)
# 		self.NumberLine.setGeometry(QtCore.QRect(10, 10, 431, 111))
# 		font = QtGui.QFont()
# 		font.setFamily("Rockwell Extra Bold")
# 		font.setPointSize(24)
# 		font.setBold(True)
# 		font.setWeight(75)
# 		self.NumberLine.setFont(font)
# 		self.NumberLine.setStyleSheet("background-color:#FF1493;\n"
# "border: 5px solid grey    ;\n"
# "border-radius: 10")
# 		self.NumberLine.setAlignment(QtCore.Qt.AlignCenter)
# 		self.NumberLine.setReadOnly(True)
# 		self.NumberLine.setObjectName("NumberLine")
# 		self.QuestionLine = QtWidgets.QLineEdit(self.TaskWidget)
# 		self.QuestionLine.setGeometry(QtCore.QRect(150, 129, 611, 231))
# 		font = QtGui.QFont()
# 		font.setFamily("Tw Cen MT Condensed Extra Bold")
# 		font.setPointSize(150)
# 		self.QuestionLine.setFont(font)
# 		self.QuestionLine.setStyleSheet("background-color:#4682B4;\n"
# "border-radius: 10;\n"
# "border: 5px solid #40E0D0    ;")
# 		self.QuestionLine.setAlignment(QtCore.Qt.AlignCenter)
# 		self.QuestionLine.setReadOnly(True)
# 		self.QuestionLine.setObjectName("QuestionLine")
# 		Task.setCentralWidget(self.TaskWidget)

# 		self.retranslateUi(Task)
# 		QtCore.QMetaObject.connectSlotsByName(Task)

# 	def retranslateUi(self, Task):
# 		_translate = QtCore.QCoreApplication.translate
# 		Task.setWindowTitle(_translate("Task", "MainWindow "))
# 		self.AnswerButton.setText(_translate("Task", "Answer  "))
 
#! треба тут вставити звичаний код 













# -*- coding: cp1251 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Task(object):
    def setupUi(self, Task):
        Task.setObjectName("Task")
        Task.setEnabled(True)
        Task.resize(920, 795)
        
        # Головний віджет
        self.TaskWidget = QtWidgets.QWidget(Task)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.TaskWidget.sizePolicy().hasHeightForWidth())
        self.TaskWidget.setSizePolicy(sizePolicy)
        self.TaskWidget.setStyleSheet("background-color: #f0f0f0;")  # Змінено фон на світло-сірий
        self.TaskWidget.setObjectName("TaskWidget")
        
        # Кнопка "Answer"
        self.AnswerButton = QtWidgets.QPushButton(self.TaskWidget)
        self.AnswerButton.setGeometry(QtCore.QRect(320, 550, 250, 120))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.AnswerButton.setFont(font)
        self.AnswerButton.setStyleSheet("""
            QPushButton {
                background-color: #007BFF; /* Синя кнопка */
                color: white;
                border-radius: 15px;
                border: 2px solid #0056b3;
            }
            QPushButton:pressed {
                background-color: #0056b3; /* Темніший при натисканні */
            }
            QPushButton:hover {
                background-color: #3399FF; /* Світліший при наведенні */
            }
        """)
        self.AnswerButton.setObjectName("AnswerButton")
        
        # Поле для введення відповіді
        self.AnswerLine = QtWidgets.QLineEdit(self.TaskWidget)
        self.AnswerLine.setGeometry(QtCore.QRect(290, 380, 311, 141))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.AnswerLine.setFont(font)
        self.AnswerLine.setStyleSheet("""
            QLineEdit {
                background-color: #FFD700; /* Жовтий фон */
                border-radius: 15px;
                border: 3px solid #FF4500; /* Червона рамка */
                color: #000000; /* Чорний текст */
            }
        """)
        self.AnswerLine.setAlignment(QtCore.Qt.AlignCenter)
        self.AnswerLine.setObjectName("AnswerLine")
        
        # Поле з номером завдання
        self.NumberLine = QtWidgets.QLineEdit(self.TaskWidget)
        self.NumberLine.setGeometry(QtCore.QRect(10, 10, 431, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.NumberLine.setFont(font)
        self.NumberLine.setStyleSheet("""
            QLineEdit {
                background-color: #FF69B4; /* Яскраво-рожевий фон */
                border: 3px solid #808080; /* Сіра рамка */
                border-radius: 15px;
                color: white; /* Білий текст */
            }
        """)
        self.NumberLine.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberLine.setReadOnly(True)
        self.NumberLine.setObjectName("NumberLine")
        
        # Поле з питанням
        self.QuestionLine = QtWidgets.QLineEdit(self.TaskWidget)
        self.QuestionLine.setGeometry(QtCore.QRect(150, 129, 611, 231))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(150)
        font.setBold(True)
        font.setWeight(75)
        self.QuestionLine.setFont(font)
        self.QuestionLine.setStyleSheet("""
            QLineEdit {
                background-color: #4682B4; /* Синьо-зелений фон */
                border-radius: 15px;
                border: 3px solid #40E0D0; /* Бірюзова рамка */
                color: white; /* Білий текст */
            }
        """)
        self.QuestionLine.setAlignment(QtCore.Qt.AlignCenter)
        self.QuestionLine.setReadOnly(True)
        self.QuestionLine.setObjectName("QuestionLine")
        
        Task.setCentralWidget(self.TaskWidget)

        self.retranslateUi(Task)
        QtCore.QMetaObject.connectSlotsByName(Task)

    def retranslateUi(self, Task):
        _translate = QtCore.QCoreApplication.translate
        Task.setWindowTitle(_translate("Task", "MainWindow"))
        self.AnswerButton.setText(_translate("Task", "Answer"))


# Запуск програми
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    task_window = QtWidgets.QMainWindow()
    ui = Ui_Task()
    ui.setupUi(task_window)
    task_window.show()
    sys.exit(app.exec_())

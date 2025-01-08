# # -*- coding: cp1251 -*-

# from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_T_Fwindow(object):
#     def setupUi(self, T_Fwindow):
#         T_Fwindow.setObjectName("T_Fwindow")
#         T_Fwindow.setEnabled(True)
#         T_Fwindow.resize(920, 795)
#         T_Fwindow.setStyleSheet("background-color: #808080")
#         self.T_Fwidget = QtWidgets.QWidget(T_Fwindow)
#         self.T_Fwidget.setObjectName("T_Fwidget")
#         self.NextButton = QtWidgets.QPushButton(self.T_Fwidget)
#         self.NextButton.setGeometry(QtCore.QRect(480, 560, 300, 150))
#         font = QtGui.QFont()
#         font.setPointSize(25)
#         font.setBold(True)
#         font.setWeight(75)
#         self.NextButton.setFont(font)
#         self.NextButton.setStyleSheet("QPushButton{\n"
# "    background-color: #808080;    \n"
# "    border-radius:10;\n"
# "color: #00008B;\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color:#00bfff;\n"
# "}")
#         self.NextButton.setObjectName("NextButton")
#         self.Tline = QtWidgets.QLineEdit(self.T_Fwidget)
#         self.Tline.setGeometry(QtCore.QRect(30, 250, 851, 231))
#         font = QtGui.QFont()
#         font.setPointSize(72)
#         font.setBold(True)
#         font.setWeight(75)
#         self.Tline.setFont(font)
#         self.Tline.setStyleSheet("background-color:#4682B4;\n"
# "border-radius: 10;\n"
# "border: 5px solid #40E0D0")
#         self.Tline.setText("")
#         self.Tline.setAlignment(QtCore.Qt.AlignCenter)
#         self.Tline.setReadOnly(True)
#         self.Tline.setObjectName("Tline")
#         self.EndButton = QtWidgets.QPushButton(self.T_Fwidget)
#         self.EndButton.setGeometry(QtCore.QRect(120, 560, 300, 150))
#         font = QtGui.QFont()
#         font.setPointSize(25)
#         font.setBold(True)
#         font.setWeight(75)
#         self.EndButton.setFont(font)
#         self.EndButton.setStyleSheet("QPushButton{\n"
# "    background-color: #808080;    \n"
# "    border-radius:10;\n"
# "color: #8B0000;\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color:#00bfff;\n"
# "}")
#         self.EndButton.setObjectName("EndButton")
#         self.T_Fline = QtWidgets.QLineEdit(self.T_Fwidget)
#         self.T_Fline.setGeometry(QtCore.QRect(30, 30, 851, 231))
#         font = QtGui.QFont()
#         font.setPointSize(72)
#         font.setBold(True)
#         font.setWeight(75)
#         self.T_Fline.setFont(font)
#         self.T_Fline.setStyleSheet("background-color:#4682B4;\n"
# "border-radius: 10;\n"
# "border: 5px solid #40E0D0")
#         self.T_Fline.setText("")
#         self.T_Fline.setAlignment(QtCore.Qt.AlignCenter)
#         self.T_Fline.setReadOnly(True)
#         self.T_Fline.setObjectName("T_Fline")
#         T_Fwindow.setCentralWidget(self.T_Fwidget)

#         self.retranslateUi(T_Fwindow)
#         QtCore.QMetaObject.connectSlotsByName(T_Fwindow)

#     def retranslateUi(self, T_Fwindow):
#         _translate = QtCore.QCoreApplication.translate
#         T_Fwindow.setWindowTitle(_translate("T_Fwindow", "MainWindow"))
#         self.NextButton.setText(_translate("T_Fwindow", "Continue\n  "
# "testing"))
#         self.EndButton.setText(_translate("T_Fwindow", "click to end \n "
# "testing"))




from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_T_Fwindow(object):
    def setupUi(self, T_Fwindow):
        T_Fwindow.setObjectName("T_Fwindow")
        T_Fwindow.setEnabled(True)
        T_Fwindow.resize(920, 795)
        T_Fwindow.setStyleSheet("background-color: #2f2f2f;")  # Темний фон для всього вікна
        self.T_Fwidget = QtWidgets.QWidget(T_Fwindow)
        self.T_Fwidget.setObjectName("T_Fwidget")

        # Кнопка "Next"
        self.NextButton = QtWidgets.QPushButton(self.T_Fwidget)
        self.NextButton.setGeometry(QtCore.QRect(480, 560, 300, 150))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.NextButton.setFont(font)
        self.NextButton.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;
                color: white;
                border-radius: 20px;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5A9BD5;
            }
            QPushButton:pressed {
                background-color: #3E7BA7;
            }
        """)
        self.NextButton.setObjectName("NextButton")

        # Поле вводу Tline
        self.Tline = QtWidgets.QLineEdit(self.T_Fwidget)
        self.Tline.setGeometry(QtCore.QRect(30, 250, 851, 231))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        self.Tline.setFont(font)
        self.Tline.setStyleSheet("""
            background-color: #4682B4;
            border-radius: 20px;
            border: 3px solid #40E0D0;
            color: white;
            padding: 15px;
        """)
        self.Tline.setText("")
        self.Tline.setAlignment(QtCore.Qt.AlignCenter)
        self.Tline.setReadOnly(True)
        self.Tline.setObjectName("Tline")

        # Кнопка "End"
        self.EndButton = QtWidgets.QPushButton(self.T_Fwidget)
        self.EndButton.setGeometry(QtCore.QRect(120, 560, 300, 150))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.EndButton.setFont(font)
        self.EndButton.setStyleSheet("""
            QPushButton {
                background-color: #8B0000;
                color: white;
                border-radius: 20px;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #B42A2A;
            }
            QPushButton:pressed {
                background-color: #5A1C1C;
            }
        """)
        self.EndButton.setObjectName("EndButton")

        # Поле вводу T_Fline
        self.T_Fline = QtWidgets.QLineEdit(self.T_Fwidget)
        self.T_Fline.setGeometry(QtCore.QRect(30, 30, 851, 231))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        self.T_Fline.setFont(font)
        self.T_Fline.setStyleSheet("""
            background-color: #4682B4;
            border-radius: 20px;
            border: 3px solid #40E0D0;
            color: white;
            padding: 15px;
        """)
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
        self.NextButton.setText(_translate("T_Fwindow", "Continue\n  testing"))
        self.EndButton.setText(_translate("T_Fwindow", "click to end \n testing"))

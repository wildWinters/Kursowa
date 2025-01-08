# # -*- coding: cp1251 -*-

# from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_MainMenuWindow(object):
#     def setupUi(self, MainMenuWindow):
#         MainMenuWindow.setObjectName("MainMenuWindow")
#         MainMenuWindow.resize(920, 795)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         MainMenuWindow.setFont(font)
#         MainMenuWindow.setStyleSheet("background-color:#00aa00")
#         self.MainMenu = QtWidgets.QWidget(MainMenuWindow)
#         self.MainMenu.setObjectName("MainMenu")
#         self.MMframe = QtWidgets.QFrame(self.MainMenu)
#         self.MMframe.setGeometry(QtCore.QRect(-40, -10, 971, 261))
#         self.MMframe.setStyleSheet("background-color: yellow")
#         self.MMframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.MMframe.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.MMframe.setObjectName("MMframe")
#         self.MMlable = QtWidgets.QLabel(self.MMframe)
#         self.MMlable.setGeometry(QtCore.QRect(250, 30, 740, 210))
#         font = QtGui.QFont()
#         font.setPointSize(24)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMlable.setFont(font)
#         self.MMlable.setStyleSheet("color: black\n"
# "")
#         self.MMlable.setObjectName("MMlable")
#         self.MMbutton10 = QtWidgets.QPushButton(self.MainMenu)
#         self.MMbutton10.setGeometry(QtCore.QRect(700, 600, 146, 140))
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton10.setFont(font)
#         self.MMbutton10.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton10.setObjectName("MMbutton10")
#         self.MMbuttonAll = QtWidgets.QPushButton(self.MainMenu)
#         self.MMbuttonAll.setGeometry(QtCore.QRect(80, 600, 146, 140))
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbuttonAll.setFont(font)
#         self.MMbuttonAll.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbuttonAll.setObjectName("MMbuttonAll")
#         self.splitter_4 = QtWidgets.QSplitter(self.MainMenu)
#         self.splitter_4.setGeometry(QtCore.QRect(240, 310, 451, 431))
#         self.splitter_4.setOrientation(QtCore.Qt.Vertical)
#         self.splitter_4.setObjectName("splitter_4")
#         self.splitter = QtWidgets.QSplitter(self.splitter_4)
#         self.splitter.setOrientation(QtCore.Qt.Horizontal)
#         self.splitter.setObjectName("splitter")
#         self.MMbutton1 = QtWidgets.QPushButton(self.splitter)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton1.setFont(font)
#         self.MMbutton1.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton1.setObjectName("MMbutton1")
#         self.MMbutton2 = QtWidgets.QPushButton(self.splitter)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton2.setFont(font)
#         self.MMbutton2.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton2.setObjectName("MMbutton2")
#         self.MMbutton3 = QtWidgets.QPushButton(self.splitter)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton3.setFont(font)
#         self.MMbutton3.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton3.setObjectName("MMbutton3")
#         self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
#         self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
#         self.splitter_2.setObjectName("splitter_2")
#         self.MMbutton4 = QtWidgets.QPushButton(self.splitter_2)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton4.setFont(font)
#         self.MMbutton4.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton4.setObjectName("MMbutton4")
#         self.MMbutton5 = QtWidgets.QPushButton(self.splitter_2)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton5.setFont(font)
#         self.MMbutton5.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton5.setObjectName("MMbutton5")
#         self.MMbutton6 = QtWidgets.QPushButton(self.splitter_2)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton6.setFont(font)
#         self.MMbutton6.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton6.setObjectName("MMbutton6")
#         self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
#         self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
#         self.splitter_3.setObjectName("splitter_3")
#         self.MMbutton7 = QtWidgets.QPushButton(self.splitter_3)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton7.setFont(font)
#         self.MMbutton7.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton7.setObjectName("MMbutton7")
#         self.MMbutton8 = QtWidgets.QPushButton(self.splitter_3)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton8.setFont(font)
#         self.MMbutton8.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton8.setObjectName("MMbutton8")
#         self.MMbutton9 = QtWidgets.QPushButton(self.splitter_3)
#         font = QtGui.QFont()
#         font.setPointSize(70)
#         font.setBold(True)
#         font.setWeight(75)
#         self.MMbutton9.setFont(font)
#         self.MMbutton9.setStyleSheet("QPushButton{\n"
# "   color: black;\n"
# "\n"
# "    background-color: blue;\n"
# "\n"
# "   border-radius: 10;\n"
# "}\n"
# "\n"
# "QPushButton:pressed{\n"
# "   background-color:#00bfff;\n"
# "}")
#         self.MMbutton9.setObjectName("MMbutton9")
#         MainMenuWindow.setCentralWidget(self.MainMenu)

#         self.retranslateUi(MainMenuWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

#     def retranslateUi(self, MainMenuWindow):
#         _translate = QtCore.QCoreApplication.translate

#         MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "MainWindow"))
#         self.MMlable.setText(_translate("MainMenuWindow", "On which number would you like\n"
# "to test your knowledge of the\n"
# "multiplication table?"))
#         self.MMbutton10.setText(_translate("MainMenuWindow", "10"))
#         self.MMbuttonAll.setText(_translate("MainMenuWindow", "Full\n"
# "Table"))
#         self.MMbutton1.setText(_translate("MainMenuWindow", "1"))
#         self.MMbutton2.setText(_translate("MainMenuWindow", "2"))
#         self.MMbutton3.setText(_translate("MainMenuWindow", "3"))
#         self.MMbutton4.setText(_translate("MainMenuWindow", "4"))
#         self.MMbutton5.setText(_translate("MainMenuWindow", "5"))
#         self.MMbutton6.setText(_translate("MainMenuWindow", "6"))
#         self.MMbutton7.setText(_translate("MainMenuWindow", "7"))
#         self.MMbutton8.setText(_translate("MainMenuWindow", "8"))
#         self.MMbutton9.setText(_translate("MainMenuWindow", "9"))





























from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(920, 795)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainMenuWindow.setFont(font)

        # Фон із градієнтом
        MainMenuWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));"
        )

        self.MainMenu = QtWidgets.QWidget(MainMenuWindow)
        self.MainMenu.setObjectName("MainMenu")

        # Верхній заголовок
        self.MMframe = QtWidgets.QFrame(self.MainMenu)
        self.MMframe.setGeometry(QtCore.QRect(0, 0, 920, 150))
        self.MMframe.setStyleSheet("background-color: rgba(255, 223, 186, 255);")
        self.MMframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MMframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MMframe.setObjectName("MMframe")

        # Текст у центрі
        self.MMlable = QtWidgets.QLabel(self.MMframe)
        self.MMlable.setGeometry(QtCore.QRect(0, 0, 920, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.MMlable.setFont(font)
        self.MMlable.setStyleSheet("color: #333333;")
        self.MMlable.setAlignment(QtCore.Qt.AlignCenter)  # Вирівнювання по центру
        self.MMlable.setObjectName("MMlable")

        # Кнопка 10
        self.MMbutton10 = QtWidgets.QPushButton(self.MainMenu)
        self.MMbutton10.setGeometry(QtCore.QRect(700, 600, 146, 140))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.MMbutton10.setFont(font)
        self.MMbutton10.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: #007BFF;
                border-radius: 20px;
                border: none;
                font-family: 'Arial';
            }
            QPushButton:pressed {
                background-color: #0056b3;
            }
            QPushButton:hover {
                background-color: #3399FF;
            }
        """)
        self.MMbutton10.setObjectName("MMbutton10")

        # Кнопка повної таблиці
        self.MMbuttonAll = QtWidgets.QPushButton(self.MainMenu)
        self.MMbuttonAll.setGeometry(QtCore.QRect(80, 600, 146, 140))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.MMbuttonAll.setFont(font)
        self.MMbuttonAll.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: #28a745;
                border-radius: 20px;
                border: none;
                font-family: 'Arial';
            }
            QPushButton:pressed {
                background-color: #218838;
            }
            QPushButton:hover {
                background-color: #34ce57;
            }
        """)
        self.MMbuttonAll.setObjectName("MMbuttonAll")

        # Блок кнопок чисел
        self.splitter_4 = QtWidgets.QSplitter(self.MainMenu)
        self.splitter_4.setGeometry(QtCore.QRect(240, 310, 451, 431))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")

        # Ряд 1
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.MMbutton1 = self.create_number_button(self.splitter, "1")
        self.MMbutton2 = self.create_number_button(self.splitter, "2")
        self.MMbutton3 = self.create_number_button(self.splitter, "3")

        # Ряд 2
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.MMbutton4 = self.create_number_button(self.splitter_2, "4")
        self.MMbutton5 = self.create_number_button(self.splitter_2, "5")
        self.MMbutton6 = self.create_number_button(self.splitter_2, "6")

        # Ряд 3
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.MMbutton7 = self.create_number_button(self.splitter_3, "7")
        self.MMbutton8 = self.create_number_button(self.splitter_3, "8")
        self.MMbutton9 = self.create_number_button(self.splitter_3, "9")

        MainMenuWindow.setCentralWidget(self.MainMenu)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def create_number_button(self, parent, text):
        """Функція для створення кнопки чисел."""
        button = QtWidgets.QPushButton(parent)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        button.setFont(font)
        button.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: #17a2b8;
                border-radius: 20px;
                border: none;
                font-family: 'Arial';
            }
            QPushButton:pressed {
                background-color: #117a8b;
            }
            QPushButton:hover {
                background-color: #20c997;
            }
        """)
        button.setText(text)
        button.setObjectName(f"MMbutton{text}")
        return button

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "MainWindow"))
        self.MMlable.setText(_translate("MainMenuWindow", "On which number would you like\n"
                                                          "to test your knowledge of the\n"
                                                          "multiplication table?"))
        self.MMbutton10.setText(_translate("MainMenuWindow", "10"))
        self.MMbuttonAll.setText(_translate("MainMenuWindow", "Full\nTable"))

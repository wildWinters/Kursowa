# -*- coding: cp1251 -*-
# -*- coding: utf-8 -*-

# sys.exit(app.exec())
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
import time
from MainMenu import Ui_MainMenuWindow
from QuestionWindow import Ui_Task
from ResultWindow import Ui_TestResultWindow
from T_Fwindow import Ui_T_Fwindow
import ctypes 

lib = ctypes.CDLL("./KursF.dll")
app = QtWidgets.QApplication(sys.argv)

# Створення головного вікна
MainMenuWindow = QtWidgets.QMainWindow()
ui = Ui_MainMenuWindow()
ui.setupUi(MainMenuWindow)
MainMenuWindow.setWindowTitle("Main Menu")  # Замість кирилиці
MainMenuWindow.setWindowIcon(QIcon("close.png"))
MainMenuWindow.show()

true_ans = 0
num = 0
start_time = 0

def openQuestionW(option):
    global start_time
    global num
    lib.writeNUM()
    num += 1
    if num == 1:
        start_time = time.time()
    global number
    number = option
    global QuestionW
    QuestionW = QtWidgets.QMainWindow()
    ui = Ui_Task()
    ui.setupUi(QuestionW)
    
    # Читання чисел з файлу
    with open("C:/numbers.txt", 'r') as file:
        numbers = file.read()
        a, b = map(int, numbers.strip().split())

    if number != 0:
        a = number
    ui.QuestionLine.setText(f'{a}*{b}')
    ui.NumberLine.setText(f'Question {num}')
    ui.AnswerLine.setPlaceholderText("___")
    QuestionW.setWindowTitle("Question")
    QuestionW.setWindowIcon(QIcon("close.png"))
    QuestionW.show()
    MainMenuWindow.hide()

    def opentf(strng):
        global tf
        tf = QtWidgets.QMainWindow()
        ui = Ui_T_Fwindow()
        ui.setupUi(tf)
        if strng == str(a * b):
            global true_ans
            true_ans += 1
            ui.T_Fline.setStyleSheet("background-color: green; border-radius: 10; border: 5px solid #40E0D0")
            ui.T_Fline.setText('Correct')
        else:
            ui.T_Fline.setStyleSheet("background-color: red; border-radius: 10; border: 5px solid #40E0D0")
            ui.T_Fline.setText('Incorrect')
        ui.Tline.setText(f'{a}*{b} = {a * b}')
        tf.setWindowTitle("True/False Window")
        tf.setWindowIcon(QIcon("close.png"))
        tf.show()
        QuestionW.close()

        def openres():
            global res
            global true_ans
            global num
            global start_time
            res = QtWidgets.QMainWindow()
            ui = Ui_TestResultWindow()
            ui.setupUi(res)
            ui.TrueAnsw.setText(str(true_ans))
            ui.QuanQuest.setText(str(num))
            ui.TimeMin.setText(str(round(((time.time() - start_time) / 60), 1)))
            res.setWindowTitle("Test Results")
            res.setWindowIcon(QIcon("close.png"))
            res.show()
            tf.close()

            def returnmain():
                global true_ans
                global num
                global start_time
                true_ans = 0
                num = 0
                start_time = 0
                res.close()
                MainMenuWindow.show()

            ui.HomeButton.clicked.connect(returnmain)

        def returnquest():
            tf.close()
            openQuestionW(number)

        ui.EndButton.clicked.connect(openres)
        ui.NextButton.clicked.connect(returnquest)

    ui.AnswerButton.clicked.connect(lambda: opentf(ui.AnswerLine.text().strip()))

# Пов'язуємо кнопки на головному екрані
ui.MMbutton1.clicked.connect(lambda: openQuestionW(1))
ui.MMbutton2.clicked.connect(lambda: openQuestionW(2))
ui.MMbutton3.clicked.connect(lambda: openQuestionW(3))
ui.MMbutton4.clicked.connect(lambda: openQuestionW(4))
ui.MMbutton5.clicked.connect(lambda: openQuestionW(5))
ui.MMbutton6.clicked.connect(lambda: openQuestionW(6))
ui.MMbutton7.clicked.connect(lambda: openQuestionW(7))
ui.MMbutton8.clicked.connect(lambda: openQuestionW(8))
ui.MMbutton9.clicked.connect(lambda: openQuestionW(9))
ui.MMbutton10.clicked.connect(lambda: openQuestionW(10))
ui.MMbuttonAll.clicked.connect(lambda: openQuestionW(0))

sys.exit(app.exec())

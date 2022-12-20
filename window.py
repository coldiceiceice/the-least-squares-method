from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
import matLine


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 557)
        MainWindow.setMinimumSize(QtCore.QSize(685, 557))
        MainWindow.setMaximumSize(QtCore.QSize(685, 557))
        MainWindow.setStyleSheet("QPushButtons {\n"
                                 "    \n"
                                 "    background-color: rgb(255, 170, 127);\n"
                                 "\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_poryadok = QtWidgets.QLabel(self.centralwidget)
        self.label_poryadok.setGeometry(QtCore.QRect(20, 20, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_poryadok.setFont(font)
        self.label_poryadok.setStyleSheet("color: white;\n"
                                          "background: rgb(0, 255, 255);\n"
                                          "font: 700 20pt \"Yu Gothic UI\";\n"
                                          "border: 3px solid rgb(0, 170, 255);\n"
                                          "border-radius: 25px")
        self.label_poryadok.setObjectName("label_poryadok")
        self.but_kvadrat = QtWidgets.QPushButton(self.centralwidget)
        self.but_kvadrat.setGeometry(QtCore.QRect(10, 340, 331, 41))
        self.but_kvadrat.setStyleSheet("QPushButton {\n"
                                       "    border: 3px solid rgb(0, 170, 255);\n"
                                       "    border-radius: 20px;\n"
                                       "    color: white;\n"
                                       "    background-color: rgb(0, 170, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(255, 0, 127);\n"
                                       "    border: 2px solid rgb(255,0,127);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: rgb(154, 0, 77);\n"
                                       "}")
        self.but_kvadrat.setObjectName("but_kvadrat")
        self.but_line = QtWidgets.QPushButton(self.centralwidget)
        self.but_line.setGeometry(QtCore.QRect(10, 280, 331, 41))
        self.but_line.setStyleSheet("QPushButton {\n"
                                    "    border: 3px solid rgb(0, 170, 255);\n"
                                    "    border-radius: 20px;\n"
                                    "    color: white;\n"
                                    "    background-color: rgb(0, 170, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(255, 0, 127);\n"
                                    "    border: 2px solid rgb(255,0,127);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "    background-color: rgb(154, 0, 77);\n"
                                    "}\n"
                                    "")
        self.but_line.setObjectName("but_line")
        self.but_kub = QtWidgets.QPushButton(self.centralwidget)
        self.but_kub.setGeometry(QtCore.QRect(10, 400, 331, 41))
        self.but_kub.setStyleSheet("QPushButton {\n"
                                   "    border: 3px solid rgb(0, 170, 255);\n"
                                   "    border-radius: 20px;\n"
                                   "    color: white;\n"
                                   "    background-color: rgb(0, 170, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: rgb(255, 0, 127);\n"
                                   "    border: 2px solid rgb(255,0,127);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "    background-color: rgb(154, 0, 77);\n"
                                   "}")
        self.but_kub.setObjectName("but_kub")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -20, 691, 531))
        self.background.setStyleSheet("background-color: rgb(155, 253, 255);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.enterLine = QtWidgets.QLabel(self.centralwidget)
        self.enterLine.setGeometry(QtCore.QRect(10, 90, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enterLine.setFont(font)
        self.enterLine.setStyleSheet("")
        self.enterLine.setObjectName("enterLine")
        self.lineEdit_X = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_X.setGeometry(QtCore.QRect(10, 120, 331, 51))
        self.lineEdit_X.setStyleSheet("QLineEdit{ \n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background: rgb(0, 255, 255);\n"
                                      "    font: 700 20pt \"Yu Gothic UI\";\n"
                                      "    border: 3px solid rgb(0, 170, 255);\n"
                                      "    border-radius: 25px\n"
                                      "}\n"
                                      "QLineEdit:focus{\n"
                                      "border: 3px solid rgb(255, 0, 127);\n"
                                      "}")
        self.lineEdit_X.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_X.setObjectName("lineEdit_X")
        self.lineEdit_Y = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Y.setGeometry(QtCore.QRect(10, 180, 331, 51))
        self.lineEdit_Y.setStyleSheet("QLineEdit{ \n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background: rgb(0, 255, 255);\n"
                                      "    font: 700 20pt \"Yu Gothic UI\";\n"
                                      "    border: 3px solid rgb(0, 170, 255);\n"
                                      "    border-radius: 25px\n"
                                      "}\n"
                                      "QLineEdit:focus{\n"
                                      "border: 3px solid rgb(255, 0, 127);\n"
                                      "}")
        self.lineEdit_Y.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Y.setObjectName("lineEdit_Y")
        self.but_stepen = QtWidgets.QPushButton(self.centralwidget)
        self.but_stepen.setGeometry(QtCore.QRect(350, 280, 331, 41))
        self.but_stepen.setStyleSheet("QPushButton {\n"
                                      "    border: 3px solid rgb(0, 170, 255);\n"
                                      "    border-radius: 20px;\n"
                                      "    color: white;\n"
                                      "    background-color: rgb(0, 170, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(255, 0, 127);\n"
                                      "    border: 2px solid rgb(255,0,127);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: rgb(154, 0, 77);\n"
                                      "}\n"
                                      "")
        self.but_stepen.setObjectName("but_stepen")
        self.but_logarifm = QtWidgets.QPushButton(self.centralwidget)
        self.but_logarifm.setGeometry(QtCore.QRect(350, 340, 331, 41))
        self.but_logarifm.setStyleSheet("QPushButton {\n"
                                        "    border: 3px solid rgb(0, 170, 255);\n"
                                        "    border-radius: 20px;\n"
                                        "    color: white;\n"
                                        "    background-color: rgb(0, 170, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(255, 0, 127);\n"
                                        "    border: 2px solid rgb(255,0,127);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgb(154, 0, 77);\n"
                                        "}\n"
                                        "")
        self.but_logarifm.setObjectName("but_logarifm")
        self.but_exp = QtWidgets.QPushButton(self.centralwidget)
        self.but_exp.setGeometry(QtCore.QRect(350, 400, 331, 41))
        self.but_exp.setStyleSheet("QPushButton {\n"
                                   "    border: 3px solid rgb(0, 170, 255);\n"
                                   "    border-radius: 20px;\n"
                                   "    color: white;\n"
                                   "    background-color: rgb(0, 170, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: rgb(255, 0, 127);\n"
                                   "    border: 2px solid rgb(255,0,127);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "    background-color: rgb(154, 0, 77);\n"
                                   "}\n"
                                   "")
        self.but_exp.setObjectName("but_exp")
        self.but_giperbol = QtWidgets.QPushButton(self.centralwidget)
        self.but_giperbol.setGeometry(QtCore.QRect(180, 460, 331, 41))
        self.but_giperbol.setStyleSheet("QPushButton {\n"
                                        "    border: 3px solid rgb(0, 170, 255);\n"
                                        "    border-radius: 20px;\n"
                                        "    color: white;\n"
                                        "    background-color: rgb(0, 170, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(255, 0, 127);\n"
                                        "    border: 2px solid rgb(255,0,127);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgb(154, 0, 77);\n"
                                        "}\n"
                                        "")
        self.but_giperbol.setObjectName("but_giperbol")
        self.lineEdit_XX = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_XX.setGeometry(QtCore.QRect(340, 150, 331, 51))
        self.lineEdit_XX.setStyleSheet("QLineEdit{ \n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background: rgb(0, 255, 255);\n"
                                       "    font: 700 20pt \"Yu Gothic UI\";\n"
                                       "    border: 3px solid rgb(0, 170, 255);\n"
                                       "    border-radius: 25px\n"
                                       "}\n"
                                       "QLineEdit:focus{\n"
                                       "border: 3px solid rgb(255, 0, 127);\n"
                                       "}")
        self.lineEdit_XX.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_XX.setObjectName("lineEdit_XX")
        self.enterLine_2 = QtWidgets.QLabel(self.centralwidget)
        self.enterLine_2.setGeometry(QtCore.QRect(350, 80, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enterLine_2.setFont(font)
        self.enterLine_2.setStyleSheet("")
        self.enterLine_2.setObjectName("enterLine_2")
        self.background.raise_()
        self.label_poryadok.raise_()
        self.but_kvadrat.raise_()
        self.but_line.raise_()
        self.but_kub.raise_()
        self.enterLine.raise_()
        self.lineEdit_X.raise_()
        self.lineEdit_Y.raise_()
        self.but_stepen.raise_()
        self.but_logarifm.raise_()
        self.but_exp.raise_()
        self.but_giperbol.raise_()
        self.lineEdit_XX.raise_()
        self.enterLine_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Курсовая"))
        self.label_poryadok.setText(_translate("MainWindow", "ПОРЯДОК:  "))
        self.but_kvadrat.setText(_translate("MainWindow", "КВАДРАТИЧНАЯ"))
        self.but_line.setText(_translate("MainWindow", "ЛИНЕЙНАЯ"))
        self.but_kub.setText(_translate("MainWindow", "КУБИЧЕСКАЯ"))
        self.enterLine.setText(_translate("MainWindow", "Введите начальные значения X, Y:"))
        self.lineEdit_X.setText(_translate("MainWindow", "X"))
        self.lineEdit_Y.setText(_translate("MainWindow", "Y"))
        self.but_stepen.setText(_translate("MainWindow", "СТЕПЕННОЙ"))
        self.but_logarifm.setText(_translate("MainWindow", "ЛОГАРИФМИЧЕСКИЙ"))
        self.but_exp.setText(_translate("MainWindow", "ЭКСПОНЦЕАЛЬНЫЙ"))
        self.but_giperbol.setText(_translate("MainWindow", "ГИПЕРБОЛИЧЕСКИЙ"))
        self.lineEdit_XX.setText(_translate("MainWindow", "X"))
        self.enterLine_2.setText(_translate("MainWindow", "Введите степень для степенного метода:"))
        self.menu.setTitle(_translate("MainWindow", "Данные установлены по умолчанию"))

############### КНОПКИ ########################
    def btn(self):
        self.but_line.clicked.connect(lambda: matLine.MathForm.line(self))
        self.but_kvadrat.clicked.connect(lambda: matLine.MathForm.square(self))
        #self.but_line.clicked.connect(lambda: self.line())
        #self.but_line.clicked.connect(lambda: self.line())
        #self.but_line.clicked.connect(lambda: self.line())
        #self.but_line.clicked.connect(lambda: self.line())
        #self.but_line.clicked.connect(lambda: self.line())



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(206, 295)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.number7 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 7
        self.number7.setGeometry(QtCore.QRect(0, 50, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number7.setFont(font)
        self.number7.setObjectName("number7")

        self.number8 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 8
        self.number8.setGeometry(QtCore.QRect(50, 50, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number8.setFont(font)
        self.number8.setObjectName("number8")

        self.number5 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 5
        self.number5.setGeometry(QtCore.QRect(50, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number5.setFont(font)
        self.number5.setObjectName("number5")

        self.number1 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 1
        self.number1.setGeometry(QtCore.QRect(0, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number1.setFont(font)
        self.number1.setObjectName("number1")

        self.number2 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 2
        self.number2.setGeometry(QtCore.QRect(50, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number2.setFont(font)
        self.number2.setObjectName("number2")

        self.number6 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 6
        self.number6.setGeometry(QtCore.QRect(100, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number6.setFont(font)
        self.number6.setObjectName("number6")

        self.number3 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 3
        self.number3.setGeometry(QtCore.QRect(100, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number3.setFont(font)
        self.number3.setObjectName("number3")

        self.number9 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 9
        self.number9.setGeometry(QtCore.QRect(100, 50, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number9.setFont(font)
        self.number9.setObjectName("number9")

        self.number4 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 4
        self.number4.setGeometry(QtCore.QRect(0, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number4.setFont(font)
        self.number4.setObjectName("number4")

        self.number0 = QtWidgets.QPushButton(parent=self.centralwidget)  # code for button 0
        self.number0.setGeometry(QtCore.QRect(50, 200, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number0.setFont(font)
        self.number0.setObjectName("number0")

        self.operator_divide = QtWidgets.QPushButton(parent=self.centralwidget)  # operator divide
        self.operator_divide.setGeometry(QtCore.QRect(150, 200, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operator_divide.setFont(font)
        self.operator_divide.setObjectName("operator_divide")

        self.operator_multiply = QtWidgets.QPushButton(parent=self.centralwidget)  # operator  multiply
        self.operator_multiply.setGeometry(QtCore.QRect(150, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operator_multiply.setFont(font)
        self.operator_multiply.setObjectName("operator_multiply")

        self.operatos_minus = QtWidgets.QPushButton(parent=self.centralwidget)   # operator minus
        self.operatos_minus.setGeometry(QtCore.QRect(150, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operatos_minus.setFont(font)
        self.operatos_minus.setObjectName("operatos_minus")

        self.operator_plus = QtWidgets.QPushButton(parent=self.centralwidget)  # operator plus
        self.operator_plus.setGeometry(QtCore.QRect(150, 50, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operator_plus.setFont(font)
        self.operator_plus.setObjectName("operator_plus")

        self.delete_button = QtWidgets.QPushButton(parent=self.centralwidget)  # delete button
        self.delete_button.setGeometry(QtCore.QRect(0, 200, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")

        self.equal_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equal_button.setGeometry(QtCore.QRect(100, 200, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")

        self.equation_line_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.equation_line_edit.setGeometry(QtCore.QRect(0, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.equation_line_edit.setFont(font)
        self.equation_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.equation_line_edit.setObjectName("equation_line_edit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 206, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.number7.setText(_translate("MainWindow", "7"))
        self.number8.setText(_translate("MainWindow", "8"))
        self.number5.setText(_translate("MainWindow", "5"))
        self.number1.setText(_translate("MainWindow", "1"))
        self.number2.setText(_translate("MainWindow", "2"))
        self.number6.setText(_translate("MainWindow", "6"))
        self.number3.setText(_translate("MainWindow", "3"))
        self.number9.setText(_translate("MainWindow", "9"))
        self.number4.setText(_translate("MainWindow", "4"))
        self.number0.setText(_translate("MainWindow", "0"))
        self.operator_divide.setText(_translate("MainWindow", "/"))
        self.operator_multiply.setText(_translate("MainWindow", "*"))
        self.operatos_minus.setText(_translate("MainWindow", "-"))
        self.operator_plus.setText(_translate("MainWindow", "+"))
        self.delete_button.setText(_translate("MainWindow", "DEL"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.equation_line_edit.setText(_translate("MainWindow", "10*3"))



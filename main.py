from PyQt6.QtCore import QTimer

from gui import Ui_MainWindow
from PyQt6 import QtWidgets
from time import sleep


class Custom_MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.equation_line_edit.setReadOnly(True)
        self.number0.clicked.connect(lambda: self.method_digit_buttons('0'))
        self.number1.clicked.connect(lambda: self.method_digit_buttons('1'))
        self.number2.clicked.connect(lambda: self.method_digit_buttons('2'))
        self.number3.clicked.connect(lambda: self.method_digit_buttons('3'))
        self.number4.clicked.connect(lambda: self.method_digit_buttons('4'))
        self.number5.clicked.connect(lambda: self.method_digit_buttons('5'))
        self.number6.clicked.connect(lambda: self.method_digit_buttons('6'))
        self.number7.clicked.connect(lambda: self.method_digit_buttons('7'))
        self.number8.clicked.connect(lambda: self.method_digit_buttons('8'))
        self.number9.clicked.connect(lambda: self.method_digit_buttons('9'))
        self.delete_button.clicked.connect(self.method_delete_button)
        self.operator_plus.clicked.connect(lambda: self.method_operation_buttons('+'))
        self.operatos_minus.clicked.connect(lambda: self.method_operation_buttons('-'))
        self.operator_divide.clicked.connect(lambda: self.method_operation_buttons('/'))
        self.operator_multiply.clicked.connect(lambda: self.method_operation_buttons('*'))
        self.equal_button.clicked.connect(self.method_equal_button)


    def method_delete_button(self):
        """
        Here I handle the delete button
        :return: set the text to value 0
        """

        self.equation_line_edit.setText("0")

    def method_digit_buttons(self,digit):
        """
        Here I handle button clicks just for digits
        :param digit: from 0-9
        """
        current_text = self.equation_line_edit.text()  # get de current text

        if current_text == '0':
            self.equation_line_edit.setText(digit)
        else:
            self.equation_line_edit.setText(current_text + digit)

    def method_operation_buttons(self, operation):
        """
        Here I handle button clicks just for operations
        :param operation: like +,-,/,*
        """
        current_text = self.equation_line_edit.text()

        self.equation_line_edit.setText(current_text + operation)

    def method_equal_button(self):
        current_equation = self.equation_line_edit.text()
        try:
            result = eval(current_equation)
            self.equation_line_edit.setText(str(result))
        except Exception:
            self.equation_line_edit.setText("Some error occured !")
            QTimer.singleShot(1500, self.reset_display)

    def reset_display(self):
        """
        Reset the display to '0'
        """
        self.equation_line_edit.setText('0')

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Custom_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

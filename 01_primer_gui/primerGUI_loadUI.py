from PyQt5 import QtWidgets, uic

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/frantassara/Desktop/MiPrimerGUI.ui", self)

        # Conectar señales a slots
        self.pushButton_clickMe.clicked.connect(self.say_hello)
        self.pushButton_delete.clicked.connect(self.clear_label)

    def say_hello(self):
        self.label_terminal.setText("Hola mundo")

    def clear_label(self):
        self.label_terminal.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import QThread, pyqtSignal
import pyqtgraph as pg
import serial
import serial.tools.list_ports
import sys
import random
import time

# ---------- CLASE DEL HILO ----------
class SerialThread(QThread):
    data_received = pyqtSignal(float)

    def __init__(self, port_name):
        super().__init__()
        self.port_name = port_name
        self.running = True  # Flag de control para parar el hilo

    def run(self):
        # Acá iría la conexión real al puerto serie:
        # ser = serial.Serial(self.port_name, 9600, timeout=1)
        
        while self.running:
            # Simulación de datos: genera un número aleatorio
            value = random.uniform(0, 10)
            # Si usas Arduino, descomentá:
            # line = ser.readline().decode().strip()
            # if line:
            #     try:
            #         value = float(line)
            #         self.data_received.emit(value)
            #     except ValueError:
            #         pass

            # Emite la señal con el valor recibido
            self.data_received.emit(value)
            
            # Espera 0.1 s → genera ~10 lecturas por segundo
            time.sleep(0.1)
        
        #ser.close()

    def stop(self):
        self.running = False
        self.quit()
        self.wait()


# ---------- CLASE PRINCIPAL ----------
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar el .ui generado con Qt Designer
        uic.loadUi("C:/Users/ulabceriani/Desktop/ArdPlotGUI.ui", self)

        # Buscar widgets por nombre (del .ui)
        self.comboBox_ports = self.findChild(QtWidgets.QComboBox, "comboBox_ports")
        self.pushButton_connect = self.findChild(QtWidgets.QPushButton, "pushButton_connect")
        self.plotWidget = self.findChild(pg.PlotWidget, "widget")

        self.serial_thread = None
        self.data = []
        self.max_points = 100

        # Conectar botón
        self.pushButton_connect.clicked.connect(self.connect_serial)

        # Configurar la gráfica
        self.plotWidget.plotItem.showGrid(True, True, 0.7)
        self.curve = self.plotWidget.plot(pen='y')

        self.refresh_ports()

    def refresh_ports(self):
        ports = serial.tools.list_ports.comports()
        self.comboBox_ports.clear()
        for port in ports:
            self.comboBox_ports.addItem(port.device)

    def connect_serial(self):
        if self.serial_thread is None:
            port = self.comboBox_ports.currentText()
            if port:
                self.serial_thread = SerialThread(port)
                self.serial_thread.data_received.connect(self.update_plot)
                self.serial_thread.start()
                self.pushButton_connect.setText("Desconectar")
        else:
            self.serial_thread.stop()
            self.serial_thread = None
            self.pushButton_connect.setText("Conectar")

    def update_plot(self, value):
        self.data.append(value)
        if len(self.data) > self.max_points:
            self.data = self.data[-self.max_points:]
        self.curve.setData(self.data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
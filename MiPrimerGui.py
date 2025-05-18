import sys
import numpy as np
from scipy.ndimage import gaussian_filter
from PyQt5 import QtWidgets, uic
from pyqtgraph import ImageView

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar archivo .ui
        uic.loadUi("/Users/melum/prueba3/form.ui", self)

        # Conectar botones (usar los nombres del .ui)
        self.pushButton_plot.clicked.connect(self.plot_image)
        self.pushButton_filter.clicked.connect(self.apply_filter)

        # Inicializar imagen vacía
        self.image_data = None

    def plot_image(self):
        # Crear imagen aleatoria
        self.image_data = np.random.rand(512, 512)
        self.widget.setImage(self.image_data)

    def apply_filter(self):
        if self.image_data is not None:
            filtered = gaussian_filter(self.image_data, sigma=2)
            self.widget.setImage(filtered)
        else:
            print("Primero debes plotear una imagen.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
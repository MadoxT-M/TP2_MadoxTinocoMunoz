from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QSlider, QDoubleSpinBox, QLineEdit
from PyQt6.uic import loadUi

from Fenêtres.matplotlib_canvas import MPLCanvas
from Models.main_model import FonctionModel

class MainView(QMainWindow):

    matplotlibVLayout: QVBoxLayout
    tangeanteHorizontalSlider: QSlider
    xMinimumDoubleSpinBox: QDoubleSpinBox
    xMaximumDoubleSpinBox:QDoubleSpinBox
    pointTangeancelineEdit:QLineEdit
    tauxVariationLineEdit: QLineEdit
    fonctionDeriveeLineEdit: QLineEdit
    fonctionLineEdit: QLineEdit

    def __init__(self):
        super().__init__()
        loadUi("FonctionMainWindow.ui",self)
        self.__model = FonctionModel()



from PyQt6.QtWidgets import QComboBox, QDoubleSpinBox, QMainWindow, QLineEdit, QVBoxLayout
from PyQt6.uic import loadUi

from Fenêtres.matplotlib_canvas import MPLCanvas
from Models.fonction_model import FonctionModel


class MainFenentre(QMainWindow):

    fonctionLineEdit:QLineEdit
    xMinimumDoubleSpinBox: QDoubleSpinBox
    xMaximumDoubleSpinBox: QDoubleSpinBox
    matplotlibVLayout:QVBoxLayout

    __model = FonctionModel

    def __init__(self):
        super().__init__()
        loadUi("ui/FonctionMainWindow.ui",self)

        self.__model = FonctionModel()
        self.__canvas = MPLCanvas(self.__model)
        self.matplotlibVLayout.addWidget(self.__canvas)
        self.fonctionLineEdit.editingFinished.connect(self.__fonction_modifiee)
        self.xMinimumDoubleSpinBox.editingFinished.connect(self.__x_minimum_modifiee)
        self.xMaximumDoubleSpinBox.editingFinished.connect(self.__x_maximum_modifiee)
        self.__model.fonctionchanged.connect(self.__canvas.dessiner)

    def __fonction_modifiee(self):
        self.__model.fonction = self.fonctionLineEdit.text()

    def __x_minimum_modifiee(self):
        valeur_str = self.xMinimumDoubleSpinBox.value()
        self.__model.xmin = float(valeur_str)

    def __x_maximum_modifiee(self):
        valeur_str = self.xMaximumDoubleSpinBox.value()
        self.__model.xmax = float(valeur_str)
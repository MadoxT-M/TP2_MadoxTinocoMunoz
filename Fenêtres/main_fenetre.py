from PyQt6.QtWidgets import QComboBox, QDoubleSpinBox, QMainWindow, QLineEdit, QVBoxLayout, QSlider
from PyQt6.uic import loadUi

from Fenêtres.matplotlib_canvas import MPLCanvas
from Models.fonction_model import FonctionModel


class MainFenentre(QMainWindow):

    fonctionLineEdit:QLineEdit
    xMinimumDoubleSpinBox: QDoubleSpinBox
    xMaximumDoubleSpinBox: QDoubleSpinBox
    matplotlibVLayout:QVBoxLayout
    tangeanteHorizontalSlider : QSlider

    __model = FonctionModel

    def __init__(self):
        super().__init__()
        loadUi("ui/FonctionMainWindow.ui",self)
        self.xMinimumDoubleSpinBox.setMinimum(-9999999)
        self.xMinimumDoubleSpinBox.setMaximum(99999999)
        self.xMaximumDoubleSpinBox.setMinimum(-9999999)
        self.xMaximumDoubleSpinBox.setMaximum(99999999)
        self.xMaximumDoubleSpinBox.setValue(10.0)

        self.__model = FonctionModel()
        self.__canvas = MPLCanvas(self.__model)
        self.matplotlibVLayout.addWidget(self.__canvas)
        self.fonctionLineEdit.editingFinished.connect(self.__fonction_modifiee)
        self.xMinimumDoubleSpinBox.editingFinished.connect(self.__x_minimum_modifiee)
        self.xMaximumDoubleSpinBox.editingFinished.connect(self.__x_maximum_modifiee)
        self.__model.fonctionchanged.connect(self.__canvas.dessiner)
        self.tangeanteHorizontalSlider.setMinimum(0)
        self.tangeanteHorizontalSlider.setMaximum(100)
        self.tangeanteHorizontalSlider.setValue(50)
        self.tangeanteHorizontalSlider.valueChanged.connect(self.__slider_modifie)

    def __fonction_modifiee(self):
        self.__model.fonction = self.fonctionLineEdit.text()

    def __x_minimum_modifiee(self):
        valeur_str = self.xMinimumDoubleSpinBox.value()
        self.__model.xmin = float(valeur_str)

    def __x_maximum_modifiee(self):
        valeur_str = self.xMaximumDoubleSpinBox.value()
        self.__model.xmax = float(valeur_str)

    def __slider_modifie(self, valeur_slider):
        xmin = self.__model.xmin
        xmax = self.__model.xmax
        x_valeur = xmin + (valeur_slider / 100.0) * (xmax - xmin)
        self.__model.x_curseur = x_valeur
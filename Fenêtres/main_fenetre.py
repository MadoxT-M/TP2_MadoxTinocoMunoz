from PyQt6.QtWidgets import QComboBox, QDoubleSpinBox, QMainWindow, QLineEdit, QVBoxLayout
from PyQt6.uic import loadUi

from Fenêtres.matplotlib_canvas import MPLCanvas
from Modèles.fonction_model import FonctionModel


class MainFenentre(QMainWindow):

    fonctionLineEdit:QLineEdit
    xMinimumDoubleSpinBox: QDoubleSpinBox
    yMaximumDoubleSpinBox: QDoubleSpinBox
    matplotlibVLayout:QVBoxLayout

    __model = FonctionModel

    def __init__(self):
        super().__init__()
        loadUi("ui/FonctionMainWindow.ui",self)

        self.__model = FonctionModel()
        self.__canvas = MPLCanvas(self.__model)
        self.matplotlibVLayout.addWidget(self.__canvas)
        self.fonctionLineEdit.editingFinished.connect(self.__fonction_modifiee)
        self.fonctionLineEdit.editingFinished.connect(self.__fonction_modifiee)

    def __fonction_modifiee(self):
        self.__model.fonction = self.fonctionLineEdit.text()
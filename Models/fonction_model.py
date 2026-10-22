from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QColor
import sympy as sp
import numpy as np


class FonctionModel(QObject):
    fonctionchanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__fonction: None = None
        self.__derivee: None = None
        self.__couleur: QColor
        self.__xmin: float= 0
        self.__xmax: float= 10
        self.__showgrille: bool = False

    @property
    def fonction(self):
        x = sp.symbols('x')
        y = sp.sympify(self.__fonction)

        xmin = self.__xmin
        xmax = self.__xmax

        y_numeric = sp.lambdify(x, y, 'numpy')
        x_values = np.linspace(xmin, 10, 500)
        y_values = y_numeric(x_values)
        return  y_values

    @fonction.setter
    def fonction(self, value):
        self.__fonction = value
        self.fonctionchanged.emit()

    @property
    def derivee(self):
        x = sp.symbols('x')
        y = sp.sympify(self.__fonction)

        xmin = self.__xmin
        xmax = self.__xmax

        y_derivee_symbolique = sp.diff(y,x)
        derivee_numeric = sp.lambdify(x, y_derivee_symbolique, 'numpy')

        x_values = np.linspace(xmin, 10, 500)
        y_derivee_values = derivee_numeric(x_values)

        return y_derivee_values

    @derivee.setter
    def derivee(self, value):
        self.__derivee = value

    @property
    def xmin(self):
        return self.__xmin

    @xmin.setter
    def xmin(self, value):
        if self.__xmin != value:
            self.__xmin = value
            self.fonctionchanged.emit()

    @property
    def xmax(self):
        return self.__xmax

    @xmax.setter
    def xmax(self, value):
        if self.__xmin != value:
            self.__xmin = value
            self.fonctionchanged.emit()


    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, value):
        self.__couleur = value

from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColor
import sympy as sp
import numpy as np


class FonctionModel(QObject):

    def __init__(self):
        super().__init__()
        self.__fonction: str = ""
        self.__x_min: float
        self.__x_max: float
        self.__couleur = QColor("")
        self.__ratio_tangente: float

    @property
    def fonction(self):
        return self.__fonction

    @fonction.setter
    def fonction(self, value):
        self.__fonction = value

    @property
    def x_min(self):
        return self.__x_min

    @x_min.setter
    def x_min(self, value):
        self.__x_min = value

    @property
    def x_max(self):
        return self.__x_max

    @x_max.setter
    def x_max(self, value):
        self.__x_max = value

    def calculer_graphe(self):
        x = sp.symbols('x')
        f = sp.sympify(self.__fonction)
        f_numeric = sp.lambdify(x, f, "numpy")

        x_values = np.linspace(self.__x_min, self.__x_max, 500)
        y_value = f_numeric(x_values)

        y_values = np.broadcast_to(y_value, x_values.shape)
        return x_values, y_values
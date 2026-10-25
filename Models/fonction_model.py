from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QColor
import sympy as sp
import numpy as np


class FonctionModel(QObject):
    fonctionchanged = pyqtSignal()
    curseurchanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__fonction: str = ""
        self.__derivee:None = None
        self.__derivee_str:None = None
        self.__couleur: QColor
        self.__xmin: float= 0
        self.__xmax: float= 10
        self.__x_curseur: float = 5.0
        self.__showgrille: bool = False

    @property
    def fonction(self):
        if not self.__fonction:
            return np.array([]), np.array([])
        x = sp.symbols('x')
        y = sp.sympify(self.__fonction)

        xmin = self.__xmin
        xmax = self.__xmax

        y_numeric = sp.lambdify(x, y, 'numpy')
        x_values = np.linspace(xmin, xmax, 500)
        y_values = y_numeric(x_values)
        return x_values, y_values

    @fonction.setter
    def fonction(self, value):
        self.__fonction = value
        self.fonctionchanged.emit()

    @property
    def derivee(self):
        if not self.__fonction:
            return np.array([]), np.array([])
        x = sp.symbols('x')
        y = sp.sympify(self.__fonction)

        xmin = self.__xmin
        xmax = self.__xmax
        if xmin < 0:
            xmin = 0

        y_derivee_symbolique = sp.diff(y,x)
        derivee_numeric = sp.lambdify(x, y_derivee_symbolique, 'numpy')

        x_values = np.linspace(xmin, xmax, 500)
        y_derivee_values = derivee_numeric(x_values)

        return x_values, y_derivee_values

    @derivee.setter
    def derivee(self, value):
        self.__derivee = value

    @property
    def derivee_str(self) -> str:
        if not self.__fonction:
            return ""
        x = sp.symbols('x')
        y = sp.sympify(self.__fonction)
        y_prime = sp.diff(y, x)
        return str(y_prime)

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
        if self.__xmax != value:
            self.__xmax = value
            self.fonctionchanged.emit()


    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, value):
        self.__couleur = value

    @property
    def x_curseur(self):
        return self.__x_curseur

    @x_curseur.setter
    def x_curseur(self, value):
        # S'assurer que le curseur reste bien entre xmin et xmax
        val_limites = max(self.__xmin, min(value, self.__xmax))
        if self.__x_curseur != val_limites:
            self.__x_curseur = val_limites
            self.curseurchanged.emit()

    def eval_fonction(self, x_val):
        if not self.__fonction:
            return 0.0
        x = sp.symbols('x')
        y = sp.sympify(self.__fonction)
        return float(sp.lambdify(x, y, 'numpy')(x_val))

    def eval_derivee(self, x_val):
        if not self.__fonction:
            return 0.0
        x = sp.symbols('x')
        y = sp.sympify(self.__fonction)
        y_prime = sp.diff(y, x)
        return float(sp.lambdify(x, y_prime, 'numpy')(x_val))

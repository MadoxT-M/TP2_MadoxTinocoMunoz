from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from Fenêtres.matplotlib_canvas import MatplotlibCanvas
from Models.main_model import FonctionModel



class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("FonctionMainWindow.ui",self)
        self.__model = FonctionModel()



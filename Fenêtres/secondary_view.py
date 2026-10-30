from PyQt6.QtWidgets import QDockWidget, QPushButton, QLineEdit, QListView
from PyQt6.uic import loadUi

from Models.liste_model import ListModel


class SecondaryFenetre(QDockWidget):

    supprimerPushButton: QPushButton
    ajouterPushButton: QPushButton
    enregistrerPushButton: QPushButton
    ajouterFonctionLineEdit: QLineEdit
    fonctionListView: QListView

    __model = ListModel

    def __init__(self):
        super().__init__()
        loadUi("ui/ListeFonctions.ui",self)



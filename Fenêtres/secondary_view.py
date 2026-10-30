from PyQt6.QtWidgets import QDockWidget, QPushButton, QLineEdit, QListView
from PyQt6.uic import loadUi

from Models.fonction_model import FonctionModel
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
        self.__model = ListModel(list(self.fonctions_initiales(self)))
        self.fonctionListView.setModel(self.__model)
        self.ajouterPushButton.clicked.connect(self.__ajouter_fonction)
        self.supprimerPushButton.clicked.connect(self.__supprimer_fonction)

    @staticmethod
    def fonctions_initiales(self):
        return ["x**2", "sin(x)", "cos(x)"]

    def __ajouter_fonction(self):
        fonction = self.ajouterFonctionLineEdit.text()
        if fonction:
            self.__model.add_item(fonction)
            self.ajouterFonctionLineEdit.clear()

    def __supprimer_fonction(self):
            index_selectionne = self.fonctionListView.currentIndex()
            if index_selectionne.isValid():
                self.__model.remove_item(index_selectionne.row())
        

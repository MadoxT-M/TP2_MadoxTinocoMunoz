from PyQt6.QtCore import pyqtSignal, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QDockWidget, QPushButton, QLineEdit, QListView
from PyQt6.uic import loadUi
from Models.liste_model import ListModel
import sympy as sp


class SecondaryFenetre(QDockWidget):
    fonctionsEnregistrees = pyqtSignal(list)

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

        ##Validateur
        regex = QRegularExpression(r"^[0-9x\s\+\-\*\/\^\(\)\.a-zA-Z]*$")
        validator = QRegularExpressionValidator(regex, self.ajouterFonctionLineEdit)
        self.ajouterFonctionLineEdit.setValidator(validator)
        self.ajouterFonctionLineEdit.textChanged.connect(self.__verifier_texte_temps_reel)

        ##Fonctionnalité des QPushButtons
        self.ajouterPushButton.clicked.connect(self.__ajouter_fonction)
        self.supprimerPushButton.clicked.connect(self.__supprimer_fonction)
        self.enregistrerPushButton.clicked.connect(self.__enregistrer_fonction)
        self.__enregistrer_fonction()

    @staticmethod
    def fonctions_initiales(self):
        return ["x**2", "sin(x)", "cos(x)"]

    def __verifier_texte_temps_reel(self, texte: str):
        texte = texte.strip()
        if not texte:
            self.ajouterFonctionLineEdit.setStyleSheet("")
            return
        try:
            x = sp.symbols('x')
            sp.sympify(texte)
            self.ajouterFonctionLineEdit.setStyleSheet("QLineEdit { background-color: #e6ffe6; }")
        except Exception:
            self.ajouterFonctionLineEdit.setStyleSheet("QLineEdit { background-color: #ffcccc; }")

    def __ajouter_fonction(self):
        fonction_str = self.ajouterFonctionLineEdit.text().strip()
        if not fonction_str:
            return

        try:
            x = sp.symbols('x')
            sp.sympify(fonction_str)
            self.__model.add_item(fonction_str)
            self.ajouterFonctionLineEdit.clear()
            self.ajouterFonctionLineEdit.setStyleSheet("")
            self.__enregistrer_fonction()

        except Exception:
            self.ajouterFonctionLineEdit.setStyleSheet("QLineEdit { background-color: #ffcccc; }")

    def __supprimer_fonction(self):
            index_selectionne = self.fonctionListView.currentIndex()
            if index_selectionne.isValid():
                self.__model.remove_item(index_selectionne.row())
                self.__enregistrer_fonction()

    def get_items(self) -> list:
        return self.__model.get_items()

    def __enregistrer_fonction(self):
        fonctions = self.__model.get_items()
        self.fonctionsEnregistrees.emit(fonctions)
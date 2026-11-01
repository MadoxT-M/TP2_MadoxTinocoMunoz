from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox, QDoubleSpinBox, QMainWindow, QLineEdit, QVBoxLayout, QSlider, QLabel, QCheckBox
from PyQt6.uic import loadUi
from sympy import true

from Fenêtres.matplotlib_canvas import MPLCanvas
from Fenêtres.secondary_view import SecondaryFenetre
from Models.fonction_model import FonctionModel


class MainFenentre(QMainWindow):
    fonctionComboBox: QComboBox
    xMinimumDoubleSpinBox: QDoubleSpinBox
    xMaximumDoubleSpinBox: QDoubleSpinBox
    matplotlibVLayout:QVBoxLayout
    tangeanteHorizontalSlider : QSlider
    grilleCheckBox: QCheckBox
    fonctionDeriveeLabel: QLabel
    fonctionTangenceLineEdit : QLineEdit
    tauxVariationLineEdit: QLineEdit



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
        self.fonctionComboBox.currentTextChanged.connect(self.__fonction_modifiee)
        self.xMinimumDoubleSpinBox.editingFinished.connect(self.__x_minimum_modifiee)
        self.xMaximumDoubleSpinBox.editingFinished.connect(self.__x_maximum_modifiee)
        self.__model.fonctionchanged.connect(self.__canvas.dessiner)
        self.__model.fonctionchanged.connect(self.__mettre_derivee_label)
        self.tangeanteHorizontalSlider.setMinimum(0)
        self.tangeanteHorizontalSlider.setMaximum(100)
        self.tangeanteHorizontalSlider.setValue(50)
        self.tangeanteHorizontalSlider.valueChanged.connect(self.__slider_modifie)
        self.__model.curseurchanged.connect(self.mettre_affichage_tangente)
        self.grilleCheckBox.toggled.connect(self.__grille_modifiee)


        self.secondary_fenetre = SecondaryFenetre()
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.secondary_fenetre)
        self.secondary_fenetre.fonctionsEnregistrees.connect(self.remplir_combobox)

        self.remplir_combobox(self.secondary_fenetre.get_items())

    def __fonction_modifiee(self, texte: str):
        self.__model.fonction = texte

    def __x_minimum_modifiee(self):
        valeur_str = self.xMinimumDoubleSpinBox.value()
        self.__model.xmin = float(valeur_str)

    def __x_maximum_modifiee(self):
        valeur_str = self.xMaximumDoubleSpinBox.value()
        self.__model.xmax = float(valeur_str)

    def __mettre_derivee_label(self):
        texte_derivee = self.__model.derivee_str
        self.fonctionDeriveeLabel.setText(texte_derivee)

    def __slider_modifie(self, valeur_slider):
        xmin = self.__model.xmin
        xmax = self.__model.xmax
        x_valeur = xmin + (valeur_slider / 100.0) * (xmax - xmin)
        self.__model.x_curseur = x_valeur

    def mettre_affichage_tangente(self):
        x = self.__model.x_curseur
        y = self.__model.eval_fonction(x)
        taux_variation = self.__model.eval_derivee(x)

        texte = f"x = {x:.2f}, y = {y:.2f}"
        self.fonctionTangenceLineEdit.setText(texte)
        texte_taux = f"{taux_variation:.2f}"
        self.tauxVariationLineEdit.setText(texte_taux)

    def __grille_modifiee(self, checked: bool):
        self.__model.showgrille = checked

    def remplir_combobox(self, liste_fonctions: list):
        premiere = self.fonctionComboBox.currentText()
        self.fonctionComboBox.clear()
        self.fonctionComboBox.addItems(liste_fonctions)
        index = self.fonctionComboBox.findText(premiere)
        if index >= 0:
            self.fonctionComboBox.setCurrentIndex(index)
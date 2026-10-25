import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
from Models.fonction_model import FonctionModel

class MPLCanvas(FigureCanvasQTAgg):
    __model = FonctionModel

    def __init__(self,model:FonctionModel):
        self.__fig, self.__ax = plt.subplots(nrows=1, ncols=2)
        self.__fig.tight_layout()
        super().__init__(self.__fig)
        self.__model = model
        self.point_func = None
        self.tangente_line = None
        self.point_deriv = None

        self.__model.fonctionchanged.connect(self.dessiner)
        self.__model.curseurchanged.connect(self.mettre_a_jour_curseur)
        self.dessiner()

    def dessiner(self):
        x_fonction, y_fonction = self.__model.fonction
        x_derivee, y_derivee = self.__model.derivee

        # Graphique 1 : Fonction
        self.__ax[0].clear()
        self.__ax[0].set_title("Fonction et Tangente")
        if len(x_fonction) > 0:
            self.__ax[0].plot(x_fonction, y_fonction, label="Fonction", color='blue')

        self.point_func, = self.__ax[0].plot([], [], 'bo')
        self.tangente_line, = self.__ax[0].plot([], [], 'blue')

        # Graphique 2 : Dérivée
        self.__ax[1].clear()
        self.__ax[1].set_title("Dérivée")
        if len(x_derivee) > 0:
            self.__ax[1].plot(x_derivee, y_derivee, label="Dérivée", color='blue')

        self.point_deriv, = self.__ax[1].plot([], [], 'bo')

        self.__fig.tight_layout()
        self.draw()
        self.mettre_a_jour_curseur()

    def mettre_a_jour_curseur(self):
        x_curseur = self.__model.x_curseur
        y_curseur = self.__model.eval_fonction(x_curseur)
        model = self.__model.eval_derivee(x_curseur)

        # 1. Mettre à jour le point sur la fonction
        self.point_func.set_data([x_curseur], [y_curseur])

        # 2. Calculer et mettre à jour la tangente
        largeur = (self.__model.xmax - self.__model.xmin) / 10.0
        if largeur == 0: largeur = 1.0
        x_tangente_vals = np.array([x_curseur - largeur, x_curseur + largeur])
        y_tangente_vals = model * (x_tangente_vals - x_curseur) + y_curseur
        self.tangente_line.set_data(x_tangente_vals, y_tangente_vals)

        # 3. Mettre à jour le point sur le graphique de la dérivée
        self.point_deriv.set_data([x_curseur], [model])
        self.draw()


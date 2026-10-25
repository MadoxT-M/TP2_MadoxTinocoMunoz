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
        self.__model.fonctionchanged.connect(self.dessiner)

    def dessiner(self):
            x_fonction, y_fonction = self.__model.fonction
            x_derivee, y_derivee = self.__model.derivee

            self.__ax[0].clear()
            if len(x_fonction) > 0:
                self.__ax[0].plot(x_fonction, y_fonction)
            self.__ax[0].set_title("Fonction")

            self.__ax[1].clear()
            if len(x_derivee) > 0:
                self.__ax[1].plot(x_derivee, y_derivee, color='orange')
            self.__ax[1].set_title("Dérivée")

            self.draw()
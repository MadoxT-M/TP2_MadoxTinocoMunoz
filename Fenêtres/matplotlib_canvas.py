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
        fonction = self.__model.fonction
        derivee = self.__model.derivee
        xmin = self.__model.xmin
        xmax = self.__model.xmax


        self.__ax[0].clear()
        self.__ax[0].plot(fonction)
        #self.__ax[0].set_xlim(xmin, xmax)

        self.__ax[1].clear()
        self.__ax[1].plot(derivee)
        #self.__ax[1].set_xlim(xmin, xmax)
        self.draw()
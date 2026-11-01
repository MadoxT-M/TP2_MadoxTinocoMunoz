import sys
import traceback

from PyQt6.QtWidgets import QApplication
from Fenêtres.main_fenetre import MainFenentre


def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype,value,tb)


if __name__ == '__main__':
    sys.excepthook = qt_exception_hook

    app = QApplication(sys.argv)
    fenetre = MainFenentre()
    fenetre.show()
    sys.exit(app.exec())


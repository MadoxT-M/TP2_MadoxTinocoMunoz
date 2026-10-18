import sys
import traceback

from PyQt6.QtWidgets import QApplication

def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype,value,tb)


if __name__ == '__main__':
    sys.excepthook = qt_exception_hook

    app = QApplication(sys.argv)
    fenetre = 


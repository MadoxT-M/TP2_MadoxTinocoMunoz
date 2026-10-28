from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt

from Models.fonction_model import FonctionModel


class ListModel(QAbstractListModel):

    __fonctions = list[FonctionModel]

    def __init__(self,fonction: list[FonctionModel]):
        super().__init__()
        self.__fonctions = fonction

    def row_count(self, parent = ...):
        return len(self.__fonctions)

    def add_item(self, item):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__fonctions.append(item)
        self.endInsertRows()

    def remove_item(self, index: int):
        self.beginRemoveRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__fonctions.pop(index)
        self.endRemoveRows()






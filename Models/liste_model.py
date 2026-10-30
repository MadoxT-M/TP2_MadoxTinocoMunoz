from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt

from Models.fonction_model import FonctionModel


class ListModel(QAbstractListModel):

    #__fonctions = list[FonctionModel]

    def __init__(self,fonctions: list = None):
        super().__init__()
        self.__fonctions = fonctions if fonctions is not None else []

    def rowCount(self, parent=QModelIndex()):
        return len(self.__fonctions)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self.__fonctions[index.row()]
        return None

    def add_item(self, item):
        position = self.rowCount()
        self.beginInsertRows(QModelIndex(), position, position)
        self.__fonctions.append(item)
        self.endInsertRows()

    def remove_item(self, index: int):
            if 0 <= index < len(self.__fonctions):
                self.beginRemoveRows(QModelIndex(), index, index)
                self.__fonctions.pop(index)
                self.endRemoveRows()
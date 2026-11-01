import json

from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
from Models.fonction_model import FonctionModel


class ListModel(QAbstractListModel):

    def __init__(self,fonctions: list = None, fichier_json: str = "fonctions.json"):
        super().__init__()
        self.__fichier_json = fichier_json
        self.__fonctions = fonctions if fonctions is not None else []
        self.charger_json()

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

    def get_items(self) -> list:
        return self.__fonctions

    def sauvegarder_json(self):
        try:
            with open(self.__fichier_json, 'w', encoding='utf-8') as fonction:
                json.dump(self.__fonctions, fonction, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde JSON : {e}")

    def charger_json(self):
        try:
            with open(self.__fichier_json, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    self.sauvegarder_json()
                else:
                    data = json.loads(content)
                    if isinstance(data, list):
                        self.__fonctions = data
        except FileNotFoundError:
            self.sauvegarder_json()
        except Exception as e:
            print(f"Erreur lors du chargement JSON : {e}")
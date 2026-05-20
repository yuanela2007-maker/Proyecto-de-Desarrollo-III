import json
import os

from model.Adoptante import Adoptante


class AdoptanteRepositorio:

    def __init__(self, filename="adoptante.json"):
        self.filename=filename

        self._lista_adoptante=[]

        self._diccionario_adoptante= {}

        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            data= json.load(file)

        for item in data:
            adoptante= Adoptante.from_dict(item)
            self._lista_adoptante.append(adoptante)
            self._diccionario_adoptante[adoptante.id_adoptante]= adoptante

    def _save(self):

        data= [adoptante.to_dict() for adoptante in self._lista_adoptante]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add(self, adoptante:Adoptante):
        self._lista_adoptante.append(adoptante)
        self._diccionario_adoptante[adoptante.id_adoptante]= adoptante
        self._save()

    def get_all(self):
        return list(self._lista_adoptante)

    def get_by_id(self, id_adoptante):
        return self._diccionario_adoptante.get(id_adoptante)

    def exists(self, id_adoptante):
        return id_adoptante in self._diccionario_adoptante

    def delete(self, id_adoptante):
        if not self.exists(id_adoptante):
            return False
        adoptante = self._diccionario_adoptante.get(id_adoptante)
        self._lista_adoptante.remove(adoptante)
        del self._diccionario_adoptante[id_adoptante]
        self._save()
        return True














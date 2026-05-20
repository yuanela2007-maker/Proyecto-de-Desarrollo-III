import os
import json

from src.model.seguimiento import Seguimiento

class SeguimientoRepository:

    def __init__(self):

        self.seguimientos = []
        self.seguimientos_por_id = {}

        self.filename = "seguimientos.py"
        self._load()

    def _load(self):

        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                seguimiento = Seguimiento.from_dict(item)

                self.seguimientos.append(seguimiento)
                self.seguimientos_por_id[seguimiento.id_seguimiento] = seguimiento

    def save(self):

        data = [solicitud.to_dict() for solicitud in self.solicitudes]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add(self, seguimiento):

        self.seguimientos.append(seguimiento)
        self.seguimientos_por_id[seguimiento.id_seguimiento] = seguimiento
        self.save()

    def delete(self, seguimiento):

        self.seguimientos.remove(seguimiento)
        del self.seguimientos_por_id[seguimiento.id_seguimiento]
        self.save()

    def get_all(self):

        return list(self.seguimientos)

    def get_all_dict(self):

        return self.seguimientos_por_id

    def get_by_id(self, id_seguimiento):

        return self.seguimientos_por_id[id_seguimiento]

    def exists(self, id_seguimiento):

        return id_seguimiento in self.seguimientos_por_id
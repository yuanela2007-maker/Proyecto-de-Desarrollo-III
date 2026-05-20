import os
import json

from src.model.solicitud import Solicitud

class SolicitudRepository:

    def __init__(self):

        self.solicitudes = []
        self.solicitudes_por_id = {}

        self.filename = "solicitudes.json"
        self._load()

    def load(self):

        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding = "utf-8") as file:
            data = json.load(file)

            for item in data:
                solicitud = Solicitud.from_dict(item)

                self.solicitudes.append(solicitud)
                self.solicitudes_por_id[solicitud.id_solicitud] = solicitud

    def save(self):

        data = [solicitud.to_dict() for solicitud in self.solicitudes]

        with open(self.filename, "w", encoding = "utf-8") as file:
            json.dump(data, file, indent = 4, ensure_ascii = False)

    def add(self, solicitud):

        self.solicitudes.append(solicitud)
        self.solicitudes_por_id[solicitud.id_solicitud] = solicitud
        self._save()

    def delete(self, solicitud):

        self.solicitudes.remove(solicitud)
        del self.solicitudes_por_id[solicitud.id_solicitud]
        self._save()

    def get_all(self):

        return list(self.solicitudes)

    def get_all_dict(self):

        return self.solicitudes_por_id

    def get_by_id(self, id_solicitud):

        return self.solicitudes_por_id[id_solicitud]

    def exists(self, id_solicitud):

        return id_solicitud in self.solicitudes_por_id




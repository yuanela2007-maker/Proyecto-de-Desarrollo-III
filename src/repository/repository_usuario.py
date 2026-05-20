import json
import os

from model.Usuario import Usuario


class UsuarioRepositorio:

    def __init__(self, filename="usuario.json"):
        self.filename=filename

        self._lista_usuario=[]

        self._diccionario_usuario= {}

        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            data= json.load(file)

        for item in data:
            usuario= Usuario.from_dict(item)
            self._lista_usuario.append(usuario)
            self._diccionario_usuario[usuario.id_usuario]= usuario

    def _save(self):

        data= [usuario.to_dict() for usuario in self._lista_usuario]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add(self, usuario:Usuario):
        self._lista_usuario.append(usuario)
        self._diccionario_usuario[usuario.id_usuario]= usuario
        self._save()

    def get_all(self):
        return list(self._lista_usuario)

    def get_by_id(self, id_usuario):
        return self._diccionario_usuario.get(id_usuario)

    def exists(self, id_usuario):
        return id_usuario in self._diccionario_usuario

    def delete(self, id_usuario):
        if not self.exists(id_usuario):
            return False
        usuario = self._diccionario_usuario.get(id_usuario)
        self._lista_usuario.remove(usuario)
        del self._diccionario_usuario[id_usuario]
        self._save()
        return True














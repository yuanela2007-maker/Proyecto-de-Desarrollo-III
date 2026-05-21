import json
import os

from model.animal import Animal


class AnimalRepositorio:

    def __init__(self, filename="animales.json"):
        self.filename = filename

        self._lista_animal = []

        self._diccionario_animal = {}

        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            animal = Animal.from_dict(item)
            self._lista_animal.append(animal)
            self._diccionario_animal[animal.id_animal] = animal

    def _save(self):
        data = [animal.to_dict() for animal in self._lista_animal]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add(self, animal: Animal):
        self._lista_animal.append(animal)
        self._diccionario_animal[animal.id_animal] = animal
        self._save()

    def get_all(self):
        return list(self._lista_animal)

    def get_by_id(self, id_animal):
        return self._diccionario_animal[id_animal]

    def exists(self, id_animal):
        return id_animal in self._diccionario_animal

    def delete(self, id_animal):
        if not self.exists(id_animal):
            return False
        animal = self._diccionario_animal[id_animal]
        self._lista_animal.remove(animal)
        del self._diccionario_animal[id_animal]
        self._save()
        return True

    def get_by_especie(self, especie):
        return [animal for animal in self._lista_animal if animal.especie.lower() == especie.lower()]

    def get_by_estado(self, estado):
        return [animal for animal in self._lista_animal if animal.estado == estado]

    def get_disponibles(self):
        return [animal for animal in self._lista_animal if animal.estado == "Disponible"]

    def get_by_nombre(self, nombre):
        return [animal for animal in self._lista_animal if nombre.lower() in animal.nombre.lower()]
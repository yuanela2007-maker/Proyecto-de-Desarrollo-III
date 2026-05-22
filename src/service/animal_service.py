from datetime import date
from src.model.animal import Animal
from src.repository.repository_animal import AnimalRepositorio

class AnimalService:

    def __init__(self):

        self.repositorio = AnimalRepositorio()

    def registrar_animal(self, id_animal, nombre, especie, raza, edad_estimada, sexo, descripcion, foto_ruta):

        if not id_animal.strip():
            raise ValueError("El ID del animal no puede estar vacío")
        if not nombre.strip():
            raise ValueError("El nombre del animal no puede estar vacío")
        if especie.lower not in("perro","gato","otro"):
            raise ValueError("La especie indicada no es válida.\nEspecies válidas: Perro, Gato y Otro")
        if not raza.strip():
            raise ValueError("La raza del animal no puede estar vacía")

        try:
            edad_estimada = int(edad_estimada)
        except:
            raise ValueError("La edad del animal debe ser numérica")

        if not sexo.strip():
            raise ValueError("El sexo del animal no puede estar vacío")
        if not descripcion.strip():
            raise ValueError("La descripción del animal no puede estar vacía")

        fecha = date.today()

        animal = Animal(id_animal, nombre, especie, raza, edad_estimada, sexo, descripcion, fecha, "Disponible", foto_ruta)
        self.repositorio.add(animal)
        return "El animal fue registrado correctamente"

    def editar_registro_animal(self, id_animal, nombre, especie, raza, edad_estimada, sexo, descripcion, foto_ruta):

        if not id_animal.strip():
            raise ValueError("El ID del animal no puede estar vacío")

        animal = self.repositorio.get_by_id(id_animal)

        if not animal:
            raise ValueError("El ID indicado no corresponde a ningún animal registrado")

        if not nombre.strip():
            raise ValueError("El nombre del animal no puede estar vacío")
        if especie.lower not in("perro","gato","otro"):
            raise ValueError("La especie indicada no es válida.\nEspecies válidas: Perro, Gato y Otro")
        if not raza.strip():
            raise ValueError("La raza del animal no puede estar vacía")

        try:
            edad_estimada = int(edad_estimada)
        except:
            raise ValueError("La edad del animal debe ser numérica")

        if not sexo.strip():
            raise ValueError("El sexo del animal no puede estar vacío")
        if not descripcion.strip():
            raise ValueError("La descripción del animal no puede estar vacía")

        animal.nombre = nombre
        animal.especie = especie
        animal.raza = raza
        animal.edad_estimada = edad_estimada
        animal.sexo = sexo
        animal.descripcion = descripcion
        animal.foto_ruta = foto_ruta

        self.repositorio._save()

    def cambiar_estado_animal(self, id_animal, estado):

        if not id_animal.strip():
            raise ValueError("El ID del animal no puede estar vacío")

        animal = self.repositorio.get_by_id(id_animal)
        if not animal:
            raise ValueError("El ID indicado no corresponde a ningún animal registrado")

        if estado.capitalize() not in("Disponible", "En proceso", "Adoptado", "En cuarentena", "Fallecido"):
            raise ValueError("El estado indicado no es válido")

        animal.estado = estado
        self.repositorio._save()
        return "El estado del animal fue cambiado correctamente"














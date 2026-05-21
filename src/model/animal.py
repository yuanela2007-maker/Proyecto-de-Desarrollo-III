class Animal:

    def __init__(self, id_animal, nombre, especie, raza, edad_estimada, sexo, descripcion, fecha_ingreso, estado, foto_ruta=""):
        self.id_animal = id_animal
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad_estimada = edad_estimada
        self.sexo = sexo
        self.descripcion = descripcion
        self.fecha_ingreso = fecha_ingreso
        self.estado = estado
        self.foto_ruta = foto_ruta

    def to_dict(self):
        return {
            "id_animal": self.id_animal,
            "nombre": self.nombre,
            "especie": self.especie,
            "raza": self.raza,
            "edad_estimada": self.edad_estimada,
            "sexo": self.sexo,
            "descripcion": self.descripcion,
            "fecha_ingreso": self.fecha_ingreso,
            "estado": self.estado,
            "foto_ruta": self.foto_ruta
        }

    @classmethod
    def from_dict(cls, diccionario_animal):
        return cls(
            diccionario_animal["id_animal"],
            diccionario_animal["nombre"],
            diccionario_animal["especie"],
            diccionario_animal["raza"],
            diccionario_animal["edad_estimada"],
            diccionario_animal["sexo"],
            diccionario_animal["descripcion"],
            diccionario_animal["fecha_ingreso"],
            diccionario_animal["estado"],
            diccionario_animal.get("foto_ruta", "")  # Usa get por si no existe la clave
        )

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def __str__(self):
        return f"{self.id_animal} | {self.nombre} | {self.especie} | {self.raza} | {self.edad_estimada} | {self.sexo} | {self.descripcion} | {self.fecha_ingreso} | {self.estado} | {self.foto_ruta}"
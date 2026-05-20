class Adoptante:

    def __init__(self, id_adoptante, nombre_completo, cedula,telefono,correo,direccion,tipo_vivienda,tiene_espacio_exterior,otros_animales,estado_perfil):
        self.id_adoptante = id_adoptante
        self.nombre_completo= nombre_completo
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.tipo_vivienda = tipo_vivienda
        self.tiene_espacio_exterior = tiene_espacio_exterior
        self.otros_animales = otros_animales
        self.estado_perfil = estado_perfil

    def to_dict(self):
        return {
            "id_adoptante": self.id_adoptante,
            "nombre_completo": self.nombre_completo,
            "cedula": self.cedula,
            "telefono": self.telefono,
            "correo": self.correo,
            "direccion": self.direccion,
            "tipo_vivienda": self.tipo_vivienda,
            "tiene_espacio_exterior": self.tiene_espacio_exterior,
            "otros_animales": self.otros_animales,
            "estado_perfil": self.estado_perfil
        }

    @classmethod
    def from_dict(cls, diccionario_adoptante):
        return cls(
            diccionario_adoptante["id_adoptante"],
            diccionario_adoptante["nombre_completo"],
            diccionario_adoptante["cedula"],
            diccionario_adoptante["telefono"],
            diccionario_adoptante["correo"],
            diccionario_adoptante["direccion"],
            diccionario_adoptante["tipo_vivienda"],
            diccionario_adoptante["tiene_espacio_exterior"],
            diccionario_adoptante["otros_animales"],
            diccionario_adoptante["estado_perfil"]
        )

    def esta_activo(self):
        if not self.estado_perfil:
            return False
        else:
            return True

    def __str__(self):
        return f"{self.id_adoptante} | {self.nombre_completo} | {self.cedula} | {self.telefono} | {self.correo} | {self.direccion} | {self.tipo_vivienda} | {self.tiene_espacio_exterior} | {self.otros_animales} | {self.estado_perfil}"

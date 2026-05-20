class Usuario:

    def __init__(self, id_usuario, nombre_usuario, contrasena,rol,nombre_completo,fecha_registro):
        self.id_usuario = id_usuario
        self.nombre_usuario= nombre_usuario
        self.contrasena = contrasena
        self.rol = rol
        self.nombre_completo = nombre_completo
        self.fecha_registro = fecha_registro

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "rol": self.rol,
            "nombre_completo": self.nombre_completo,
            "fecha_registro": self.fecha_registro
        }

    @classmethod
    def from_dict(cls, diccionario_usuario):
        return cls(
            diccionario_usuario["id_usuario"],
            diccionario_usuario["nombre_usuario"],
            diccionario_usuario["contrasena"],
            diccionario_usuario["rol"],
            diccionario_usuario["nombre_completo"],
            diccionario_usuario["fecha_registro"]
        )

    def verificar_contrasena(self):
        if not self.contrasena:
            return False
        else:
            return True

    def __str__(self):
        return f"{self.id_usuario} | {self.nombre_usuario} | {self.contrasena} | {self.rol} | {self.nombre_completo} | {self.fecha_registro}"

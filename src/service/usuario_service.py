from datetime import date
from model.Usuario import Usuario

class UsuarioService:

    def __init__(self, repositorio_usuario):
        self.repositorio_usuario = repositorio_usuario

    def agregar_usuario(self, id_usuario, nombre_usuario, contrasena,rol,nombre_completo):
        if self.repositorio_usuario.exists(id_usuario):
            raise ValueError("El usuario ya existe.")
        elif not nombre_usuario or nombre_usuario.strip() == "":
            raise ValueError("El nombre de usuario debe de ser llenado.")
        elif not contrasena:
            raise ValueError("La contrasena no debe de estar vacia.")
        elif not Usuario.contrasena_es_valida(contrasena):
            raise ValueError("La contrasena debe de tener 6 o mas caracteres...")
        elif rol.lower() not in ["admin", "voluntario"]:
            raise ValueError("El rol debe ser 'admin' o 'voluntario'")
        elif not nombre_completo or nombre_completo.strip() == "":
            raise ValueError("El nombre debe de estar lleno.")
        fecha_registro=date.today()

        usuario = Usuario(id_usuario, nombre_usuario, contrasena, rol, nombre_completo, fecha_registro)
        self.repositorio_usuario.add(usuario)
        return True, "Usuario registrado correctamente"

    def get_all_usuarios(self):
        return self.repositorio_usuario.get_all()

    def get_usuario_by_id(self, id_usuario):
        if not self.repositorio_usuario.exists(id_usuario):
            raise ValueError(f"El usuario con ID {id_usuario} no existe.")
        return self.repositorio_usuario.get_by_id(id_usuario), ""

    def delete_usuario(self, id_usuario):
        if not self.repositorio_usuario.exists(id_usuario):
            raise ValueError(f"El usuario con ID {id_usuario} no existe, por ende no se puede borrar.")
        self.repositorio_usuario.delete(id_usuario)
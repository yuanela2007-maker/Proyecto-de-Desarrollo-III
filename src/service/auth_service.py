class AuthService:
    def __init__(self, repositorio_usuario):
        self.repositorio_usuario = repositorio_usuario

    def autenticar(self, nombre_usuario, contrasena):
        usuario = self.repositorio_usuario.get_usuario_by_nombre_usuario(nombre_usuario)
        if not usuario:
            return False, "Usuario no encontrado"
        if usuario.contrasena == contrasena:
            return True, "Autenticación exitosa", usuario
        else:
            return False, "Contraseña incorrecta"

    def login(self, nombre_usuario, contrasena):
        """Autentica un usuario y retorna su información"""
        return self.autenticar(nombre_usuario, contrasena)

    def tiene_permiso_admin(self, usuario):
        """Verifica si el usuario tiene rol de admin"""
        if not usuario:
            return False
        return usuario.rol == "admin"

    def tiene_permiso_voluntario(self, usuario):
        """Verifica si el usuario tiene rol de voluntario"""
        if not usuario:
            return False
        return usuario.rol == "voluntario"

    def puede_aprobar_solicitudes(self, usuario):
        """Solo administradores pueden aprobar solicitudes"""
        return self.tiene_permiso_admin(usuario)

    def puede_generar_reportes(self, usuario):
        """Solo administradores pueden generar reportes"""
        return self.tiene_permiso_admin(usuario)

    def puede_registrar_animal(self, usuario):
        """Ambos roles pueden registrar animales"""
        return usuario and usuario.rol in ["admin", "voluntario"]

    def puede_gestionar_usuarios(self, usuario):
        """Solo administradores pueden gestionar usuarios"""
        return self.tiene_permiso_admin(usuario)
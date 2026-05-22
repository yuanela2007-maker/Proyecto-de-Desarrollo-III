from repository.repository_adoptante import AdoptanteRepositorio
from repository.repository_usuario import UsuarioRepositorio
from service.adoptante_service import AdoptanteService
from service.animal_service import AnimalService
from service.auth_service import AuthService
from service.seguimiento_service import SeguimientoService
from service.solicitud_service import SolicitudService
from service.usuario_service import UsuarioService

class AppController:

    def __init__(self):

        self.repositorio_adoptantes = AdoptanteRepositorio()
        self.repositorio_usuarios = UsuarioRepositorio()

        self.servicio_animales = AnimalService()
        self.servicio_adoptantes = AdoptanteService(self.repositorio_adoptantes)
        self.servicio_autenticacion = AuthService(self.repositorio_usuarios)
        self.servicio_usuarios = UsuarioService(self.repositorio_usuarios)
        self.servicio_solicitudes = SolicitudService(self.servicio_animales.repositorio, self.servicio_adoptantes.repositorio_adoptante)
        self.servicio_seguimientos = SeguimientoService(self.servicio_solicitudes.repositorio, self.servicio_usuarios.repositorio_usuario)

    def registrar_solicitud(self, id_solicitud, id_adoptante, id_animal):

        try:
            mensaje = self.servicio_solicitudes.registrar_solicitud(id_solicitud, id_adoptante, id_animal)
            return mensaje
        except ValueError as error:
            return str(error)

    def iniciar_revision_solicitud(self, id_solicitud):

        try:
            mensaje = self.servicio_solicitudes.iniciar_revision_solicitud(id_solicitud)
            return mensaje
        except ValueError as error:
            return str(error)

    def determinar_resolucion_solicitud(self, id_usuario, id_solicitud, observaciones):

        try:
            usuario = self.servicio_usuarios.get_usuario_by_id(id_usuario)

            if not self.servicio_autenticacion.tiene_permiso_admin(usuario):
                return "El usuario no está autorizado para realizar este proceso"

            mensaje = self.servicio_solicitudes.determinar_resolucion_solicitud(id_solicitud, observaciones)
            return mensaje
        except ValueError as error:
            return str(error)

    def realizar_entrega(self, id_solicitud):

        try:
            mensaje = self.servicio_solicitudes.realizar_entrega(id_solicitud)
            return mensaje
        except ValueError as error:
            return str(error)

    def registrar_seguimiento(self, id_seguimiento, id_solicitud, id_usuario, observaciones, estado_animal):

        try:
            mensaje = self.servicio_seguimientos.registrar_seguimiento(id_seguimiento, id_solicitud, id_usuario, observaciones, estado_animal)
            return mensaje
        except ValueError as error:
            return str(error)

    def obtener_historial_por_adopcion(self, id_solicitud):

        try:
            seguimientos = self.servicio_seguimientos.obtener_historial_por_adopcion(id_solicitud)
            return seguimientos
        except ValueError as error:
            return str(error)

    def marcar_seguimiento_completado(self, id_seguimiento):

        try:
            mensaje = self.servicio_seguimientos.marcar_seguimiento_completado(id_seguimiento)
            return mensaje
        except ValueError as error:
            return str(error)

    def registrar_animal(self, id_animal, nombre, especie, raza, edad_estimada, sexo, descripcion, foto_ruta):

        try:
            mensaje = self.servicio_animales.registrar_animal(id_animal, nombre, especie, raza, edad_estimada, sexo, descripcion, foto_ruta)
            return mensaje
        except ValueError as error:
            return str(error)

    def editar_registro_animal(self, id_animal, nombre, especie, raza, edad_estimada, sexo, descripcion, foto_ruta):

        try:
            mensaje = self.servicio_animales.editar_registro_animal(id_animal, nombre, especie, raza, edad_estimada, sexo, descripcion, foto_ruta)
            return mensaje
        except ValueError as error:
            return str(error)

    def cambiar_estado_animal(self, id_animal, estado):

        try:
            mensaje = self.servicio_animales.cambiar_estado_animal(id_animal, estado)
            return mensaje
        except ValueError as error:
            return str(error)

    def agregar_adoptante(self, id_adoptante, nombre_completo, cedula, telefono, correo, direccion, tipo_vivienda, tiene_espacio_exterior, otros_animales):

        try:
            agregado, mensaje = self.servicio_adoptantes.agregar_adoptante(id_adoptante, nombre_completo, cedula, telefono, correo, direccion, tipo_vivienda, tiene_espacio_exterior, otros_animales)
            return agregado, mensaje
        except ValueError as error:
            return False, str(error)

    def get_adoptante_by_id(self, id_adoptante):

        try:
            adoptante, mensaje = self.servicio_adoptantes.get_adoptante_by_id(id_adoptante)
            return adoptante, mensaje
        except ValueError as error:
            return None, str(error)

    def get_adoptante_by_cedula(self, cedula):

        try:
            adoptante, mensaje = self.servicio_adoptantes.get_adoptante_by_cedula(cedula)
            return adoptante, mensaje
        except ValueError as error:
            return None, str(error)

    def delete_adoptante(self, id_adoptante):

        try:
            eliminado, mensaje = self.servicio_adoptantes.delete_adoptante(id_adoptante)
            return eliminado, mensaje
        except ValueError as error:
            return False, str(error)

    def get_adoptantes_activos(self):

        return self.servicio_adoptantes.get_adoptantes_activos()

    def suspender_adoptante(self, id_adoptante):

        try:
            suspendido, mensaje = self.suspender_adoptante(id_adoptante, self.servicio_solicitudes)
            return suspendido, mensaje
        except ValueError as error:
            return False, str(error)

    def ver_historial_adopciones(self, id_adoptante):

        return self.servicio_adoptantes.ver_historial_adopciones(id_adoptante, self.servicio_solicitudes)

    def update_adoptante(self, id_adoptante, nombre_completo, telefono, correo, direccion, tipo_vivienda, tiene_espacio_exterior, otros_animales):

        try:
            actualizado, mensaje = self.servicio_adoptantes.update_adoptante(id_adoptante, nombre_completo, telefono, correo, direccion, tipo_vivienda, tiene_espacio_exterior, otros_animales)
            return actualizado, mensaje
        except ValueError as error:
            return False, str(error)

    def agregar_usuario(self, id_usuario, nombre_usuario, contrasena, rol, nombre_completo):

        try:
            agregado, mensaje = self.servicio_usuarios.agregar_usuario(id_usuario, nombre_usuario, contrasena, rol, nombre_completo)
            return agregado, mensaje
        except ValueError as error:
            return False, str(error)

    def autenticar(self, nombre_usuario, contrasena):

        autenticado, mensaje = self.servicio_autenticacion.autenticar(nombre_usuario, contrasena)
        return autenticado, mensaje

    def get_all_usuarios(self):

        return self.servicio_usuarios.get_all_usuarios()

    def get_usuario_by_id(self, id_usuario):

        try:
            usuario, mensaje = self.servicio_usuarios.get_usuario_by_id(id_usuario)
            return usuario, mensaje
        except ValueError as error:
            return None, str(error)

    def delete_usuario(self, id_usuario):

        try:
            self.servicio_usuarios.delete_usuario(id_usuario)
        except ValueError as error:
            return str(error)

























from datetime import date
from src.model.seguimiento import Seguimiento
from src.repository.seguimiento_repository import SeguimientoRepository

class SeguimientoService:

    def __init__(self, repositorio_solicitudes, repositorio_usuarios):

        self.repositorio = SeguimientoRepository()
        self.repositorio_solicitudes = repositorio_solicitudes
        self.repositorio_usuarios = repositorio_usuarios

    def registrar_seguimiento(self, id_seguimiento, id_solicitud, id_usuario, observaciones, estado_animal):

        if self.repositorio.exists(id_seguimiento):
            raise ValueError("El ID indicado ya pertenece a un seguimiento registrado")

        solicitud = self.repositorio_solicitudes.get_by_id(id_solicitud)

        if not solicitud:
            raise ValueError("El ID no pertenece a ninguna solicitud registrado")

        usuario = self.repositorio_usuarios.get_by_id(id_usuario)

        if not usuario:
            raise ValueError("El ID no pertenece a ningún usuario registrado")

        if estado_animal in ("Regular", "Preocupante"):
            requiere_visita = True

        fecha = date.today()

        seguimiento = Seguimiento(id_seguimiento, fecha, id_usuario, usuario.nombre_usuario, observaciones, estado_animal, False)
        self.repositorio.add(seguimiento)
        return "El seguimiento se registró correctamente"

    def obtener_historial_por_adopcion(self, id_solicitud):

        solicitud = self.repositorio_solicitudes.get_by_id(id_solicitud)

        if not solicitud:
            raise ValueError("El ID indicado no pertenece a ninguna solicitud de adopción registrada")

        if solicitud.estado != "Entregada":
            raise ValueError("La solicitud de adopción indicada no tiene una entrega realizada")

        seguimientos_por_adopcion = []
        seguimientos = self.repositorio.get_all()

        for seguimiento in seguimientos:
            if seguimiento.id_solicitud == id_solicitud:

            seguimientos_por_adopcion.append(seguimiento)

        return seguimientos_por_adopcion

    def marcar_seguimiento_completado(self, id_seguimiento):

        seguimiento = self.repositorio.get_by_id(id_seguimiento)

        if not seguimiento:
            raise ValueError("El ID indicado no pertenece a ningún seguimiento de adopción registrada")

        seguimiento.marcar_completado()
        return "El seguimiento se completó correctamente"


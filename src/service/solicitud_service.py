from datetime import date
from model.solicitud import Solicitud
from src.repository.solicitud_repository import SolicitudRepository

class SolicitudService:

    def __init__(self, repositorio_animales, repositorio_adoptantes):

        self.repositorio = SolicitudRepository()
        self.repositorio_animales = repositorio_animales
        self.repositorio_adoptantes = repositorio_adoptantes

    def registrar_solicitud(self, id_solicitud, id_adoptante, id_animal):

        if self.repositorio.exists(id_solicitud):
            raise ValueError("El ID indicado ya pertenece a una solicitud registrada")

        animal = self.repositorio_animales.get_by_id(id_animal)

        if not animal:
            raise ValueError("El ID indicado no corresponde a ningún animal registrado")

        if animal.estado != "Disponible":
            raise ValueError("El animal indicado no está disponible para adopción")

        adoptante = self.repositorio_adoptantes.get_by_id(id_adoptante)

        if not adoptante:
            raise ValueError("El ID indicado no corresponde a ningún adoptante registrado")

        if adoptante.estado_perfil == "Suspendido":
            raise ValueError("El adoptante indicado debe tener un perfil activo")

        fecha = date.today()

        solicitud = Solicitud(id_solicitud, fecha, id_adoptante, id_animal, "Pendiente", "Aún no se han realizado observaciones.", "Por definir", "Por definir")
        self.repositorio.add(solicitud)
        return "La solicitud fue registrada correctamente"

    def iniciar_revision_solicitud(self, id_solicitud):

        solicitud = self.repositorio.get_by_id(id_solicitud)

        if not solicitud:
            raise ValueError("El ID indicado no pertenece a ninguna solicitud registrada")

        animal = self.repositorio_animales.get_by_id(solicitud.id_animal)

        solicitud.estado = "En revisión"
        animal.estado = "En proceso"
        self.repositorio.save()
        return "La revisión de la solicitud fue iniciada correctamente"

    def determinar_resolucion_solicitud(self, id_solicitud, observaciones):

        solicitud = self.repositorio.get_by_id(id_solicitud)

        if not solicitud:
            raise ValueError("El ID indicado no pertenece a ninguna solicitud registrada")

        adoptante = self.repositorio_adoptantes.get_by_id(solicitud.id_adoptante)
        animal = self.repositorio_animales.get_by_id(solicitud.id_animal)

        if adoptante.tiene_espacio_exterior == "no":
            solicitud.estado = "Rechazada"
            animal.estado = "Disponible"
        else:
            solicitud.estado = "Aprobada"
            animal.estado = "Adoptado"

        solicitud.observaciones = observaciones
        solicitud.fecha_resolucion = date.today()
        self.repositorio.save()
        return "La resolución de la solicitud fue registrada correctamente"

    def realizar_entrega(self, id_solicitud):

        solicitud = self.repositorio.get_by_id(id_solicitud)

        if not solicitud:
            raise ValueError("El ID indicado no pertenece a ninguna solicitud registrada")

        solicitud.estado = "Entregada"
        solicitud.fecha_entrega = date.today()
        self.repositorio.save()
        return "La solicitud fue entregada correctamente"





















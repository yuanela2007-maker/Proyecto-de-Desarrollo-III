from model.Adoptante import Adoptante
class AdoptanteService:
    def __init__(self, repositorio_adoptante):
        self.repositorio_adoptante = repositorio_adoptante

    def agregar_adoptante(self, id_adoptante, nombre_completo, cedula, telefono,correo, direccion, tipo_vivienda, tiene_espacio_exterior,otros_animales, estado_perfil="Activo"):
        if self.repositorio_adoptante.exists(id_adoptante):
            raise ValueError("El ID del adoptante ya existe.")
        elif not nombre_completo or nombre_completo.strip() == "":
            raise ValueError("El nombre completo no puede estar vacío.")
        elif not cedula or cedula.strip() == "":
            raise ValueError("La cédula no puede estar vacía.")
        elif self.repositorio_adoptante.exists_cedula(cedula):
            raise ValueError("Ya existe un adoptante con esa cédula.")
        elif not telefono or telefono.strip() == "":
            raise ValueError("El teléfono no puede estar vacío.")
        elif not self.validar_telefono(telefono):
            raise ValueError("El teléfono debe tener 8 dígitos.")
        elif not correo or correo.strip() == "":
            raise ValueError("El correo no puede estar vacío.")
        elif not self.validar_correo(correo):
            raise ValueError("El formato del correo no es válido (ej: usuario@dominio.com).")
        elif not direccion or direccion.strip() == "":
            raise ValueError("La dirección no puede estar vacía.")
        elif tipo_vivienda.lower() not in ["casa", "apartamento"]:
            raise ValueError("El tipo de vivienda debe ser 'casa' o 'apartamento'.")
        elif estado_perfil.lower() not in ["activo", "suspendido"]:
            raise ValueError("El estado del perfil debe ser 'Activo' o 'Suspendido'.")

        adoptante = Adoptante(id_adoptante, nombre_completo, cedula, telefono, correo, direccion,tipo_vivienda.lower(), tiene_espacio_exterior, otros_animales, estado_perfil)

        self.repositorio_adoptante.add(adoptante)
        return True, "Adoptante registrado correctamente"

    def validar_cedula(self, cedula):
        if not cedula:
            return False
        if len(cedula) != 9:
            return False
        return cedula.isdigit()

    def validar_telefono(self, telefono):
        if not telefono:
            return False
        if len(telefono) != 8:
            return False
        return telefono.isdigit()

    def validar_correo(self, correo):
        if not correo:
            return False
        if "@" not in correo:
            return False
        return True

    def get_all_adoptantes(self):
        return self.repositorio_adoptante.get_all()

    def get_adoptante_by_id(self, id_adoptante):
        if not self.repositorio_adoptante.exists(id_adoptante):
            raise ValueError(f"El adoptante con ID {id_adoptante} no existe.")
        return self.repositorio_adoptante.get_by_id(id_adoptante), ""

    def get_adoptante_by_cedula(self, cedula):
        if not self.repositorio_adoptante.exists_cedula(cedula):
            raise ValueError(f"El adoptante con esa {cedula} no existe.")
        return self.repositorio_adoptante.get_by_cedula(cedula), ""

    def delete_adoptante(self, id_adoptante):
        if not self.repositorio_adoptante.exists(id_adoptante):
            raise ValueError(f"El adoptante con ID {id_adoptante} no existe.")
        self.repositorio_adoptante.delete(id_adoptante)
        return True, "Adoptante eliminado correctamente"


    def get_adoptantes_activos(self):
        """Lista solo adoptantes con perfil activo"""
        return [adoptante for adoptante in self.repositorio_adoptante.get_all() if adoptante.estado_perfil == "Activo"]

    def suspender_adoptante(self, id_adoptante, solicitud_service):
        adoptante = self.repositorio_adoptante.get_by_id(id_adoptante)

        if not adoptante:
            raise ValueError("El adoptante no existe.")

        if adoptante.estado_perfil == "Suspendido":
            raise ValueError("El adoptante ya se encuentra suspendido.")

        todas_solicitudes = solicitud_service.get_all_solicitudes()

        rechazadas = 0
        for solicitud in todas_solicitudes:
            if solicitud.id_adoptante == id_adoptante and solicitud.estado == "Rechazada":
                rechazadas += 1

        if rechazadas >= 3:
            adoptante.estado_perfil = "Suspendido"
            #self.repositorio_adoptante.add(adoptante)
            return True, f"Adoptante suspendido correctamente. Tenía {rechazadas} solicitudes rechazadas."
        else:
            return False, f"No se puede suspender. Solo tiene {rechazadas} rechazo(s) y se necesitan 3."

    def ver_historial_adopciones(self, id_adoptante, solicitud_service):
        todas_solicitudes = solicitud_service.get_all_solicitudes()
        historial = []
        for solicitud in todas_solicitudes:
            if solicitud.id_adoptante == id_adoptante:
                historial.append(solicitud)
        return historial



    def update_adoptante(self, id_adoptante, nombre_completo, telefono, correo, direccion, tipo_vivienda,tiene_espacio_exterior, otros_animales):
        adoptante = self.get_adoptante_by_id(id_adoptante)

        if not nombre_completo or nombre_completo.strip() == "":
            raise ValueError("El nombre completo no puede estar vacío.")

        if not self.validar_telefono(telefono):
            raise ValueError("El teléfono debe tener 8 dígitos.")

        if not self.validar_correo(correo):
            raise ValueError("El formato del correo no es válido.")

        if not direccion or direccion.strip() == "":
            raise ValueError("La dirección no puede estar vacía.")

        if tipo_vivienda.lower() not in ["casa", "apartamento"]:
            raise ValueError("El tipo de vivienda debe ser 'casa' o 'apartamento'.")

        adoptante.nombre_completo = nombre_completo
        adoptante.telefono = telefono
        adoptante.correo = correo
        adoptante.direccion = direccion
        adoptante.tipo_vivienda = tipo_vivienda.lower()
        adoptante.tiene_espacio_exterior = tiene_espacio_exterior
        adoptante.otros_animales = otros_animales

        self.repositorio_adoptante.add(adoptante)
        return True, "Adoptante actualizado correctamente"


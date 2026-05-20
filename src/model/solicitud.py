class Solicitud:

    def __init__(self, id_solicitud, fecha_solicitud, id_adoptante, id_animal, estado, observaciones, fecha_resolucion, fecha_entrega):

        self.id_solicitud = id_solicitud
        self.fecha_solicitud = fecha_solicitud
        self.id_adoptante = id_adoptante
        self.id_animal = id_animal
        self.estado = estado
        self.observaciones = observaciones
        self.fecha_resolucion = fecha_resolucion
        self.fecha_entrega = fecha_entrega

#---------------------------------------------------------------------------------------------------------------------------------------
    def to_dict(self):

        return {
            "id_solicitud": self.id_solicitud,
            "fecha_solicitud": self.fecha_solicitud,
            "id_adoptante": self.id_adoptante,
            "id_animal": self.id_animal,
            "estado": self.estado,
            "observaciones": self.observaciones,
            "fecha_resolucion": self.fecha_resolucion,
            "fecha_entrega": self.fecha_entrega
        }

#---------------------------------------------------------------------------------------------------------------------------------------
    @classmethod
    def from_dict(cls, diccionario_solicitud):

        return cls(
            diccionario_solicitud["id_solicitud"],
            diccionario_solicitud["fecha_solicitud"],
            diccionario_solicitud["id_adoptante"],
            diccionario_solicitud["id_animal"],
            diccionario_solicitud["estado"],
            diccionario_solicitud["observaciones"],
            diccionario_solicitud["fecha_resolucion"],
            diccionario_solicitud["fecha_entrega"]
        )

#---------------------------------------------------------------------------------------------------------------------------------------
    def esta_activa(self):

        if self.estado != "Rechazada":
            return False
        return True

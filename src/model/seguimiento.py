class Seguimiento:

    def __init__(self, id_seguimiento, fecha, id_solicitud, responsable, observaciones, estado_animal, requiere_visita, completado):

        self.id_seguimiento = id_seguimiento
        self.fecha = fecha
        self.id_solicitud = id_solicitud
        self.responsable = responsable
        self.observaciones = observaciones
        self.estado_animal = estado_animal
        self.requiere_visita = requiere_visita
        self.completado = completado

#-------------------------------------------------------------------------------------------------------------------------------------
    def to_dict(self):

        return {
            "id_seguimiento": self.id_seguimiento,
            "fecha": self.fecha,
            "id_solicitud": self.id_solicitud,
            "responsable": self.responsable,
            "observaciones": self.observaciones,
            "estado_animal": self.estado_animal,
            "requiere_visita": self.requiere_visita,
            "completado": self.completado
        }
#-------------------------------------------------------------------------------------------------------------------------------------
    @classmethod
    def from_dict(cls, diccionario_seguimiento):

        return cls(
            diccionario_seguimiento["id_seguimiento"],
            diccionario_seguimiento["fecha"],
            diccionario_seguimiento["id_solicitud"],
            diccionario_seguimiento["responsable"],
            diccionario_seguimiento["observaciones"],
            diccionario_seguimiento["estado_animal"],
            diccionario_seguimiento["requiere_visita"],
            diccionario_seguimiento["completado"]
        )
#-------------------------------------------------------------------------------------------------------------------------------------
    def marcar_completado(self):

        self.completado = True
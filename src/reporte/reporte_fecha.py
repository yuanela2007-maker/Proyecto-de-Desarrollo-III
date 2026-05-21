class ReporteFecha:

    def __init__(self, repositorio_solicitudes, repositorio_animales, repositorio_adoptantes):

        self.repositorio_solicitudes = repositorio_solicitudes
        self.repositorio_animales = repositorio_animales
        self.repositorio_adoptantes = repositorio_adoptantes

    def generar_reporte_adopciones(self, fecha_inicio, fecha_fin):

        solicitudes = self.repositorio_solicitudes.get_all()

        reporte = []

        total_adopciones = 0
        total_dias = 0

        for solicitud in solicitudes:

            if solicitud.estado == "Entregada":

                if solicitud.fecha_entrega >= fecha_inicio and solicitud.fecha_entrega <= fecha_fin:

                    animal = self.repositorio_animales.get_by_id(solicitud.id_animal)

                    adoptante = self.repositorio_adoptantes.get_by_id(solicitud.id_adoptante)

                    dias_albergue = (solicitud.fecha_entrega - animal.fecha_ingreso).days

                    total_dias += dias_albergue
                    total_adopciones += 1

                    datos = {

                        "id_solicitud": solicitud.id_solicitud,
                        "animal": animal.nombre,
                        "adoptante": adoptante.nombre_completo,
                        "fecha_entrega": solicitud.fecha_entrega,
                        "dias_en_albergue": dias_albergue

                    }

                    reporte.append(datos)

        promedio_dias = 0

        if total_adopciones > 0:

            promedio_dias = total_dias / total_adopciones

        return {

            "adopciones": reporte,
            "total_adopciones": total_adopciones,
            "promedio_dias": promedio_dias

        }
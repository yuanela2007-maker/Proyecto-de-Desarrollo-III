class ReporteEstado:

    def __init__(self, repositorio_animales, repositorio_solicitudes, repositorio_seguimientos):

        self.repositorio_animales = repositorio_animales
        self.repositorio_solicitudes = repositorio_solicitudes
        self.repositorio_seguimientos = repositorio_seguimientos

    def generar_reporte_estado_albergue(self):

        animales = self.repositorio_animales.get_all()

        total_animales = len(animales)

        estados = {}

        for animal in animales:

            estado = animal.estado

            if estado not in estados:

                estados[estado] = 0

            estados[estado] += 1

        reporte_estados = []

        for estado in estados:

            cantidad = estados[estado]

            porcentaje = 0

            if total_animales > 0:

                porcentaje = (cantidad / total_animales) * 100

            datos = {

                "estado": estado,
                "cantidad": cantidad,
                "porcentaje": porcentaje

            }

            reporte_estados.append(datos)

        solicitudes = self.repositorio_solicitudes.get_all()

        solicitudes_activas = 0

        for solicitud in solicitudes:

            if solicitud.estado in ("Pendiente", "En revisión", "Aprobada"):

                solicitudes_activas += 1

        seguimientos = self.repositorio_seguimientos.get_all()

        seguimientos_pendientes = 0

        for seguimiento in seguimientos:

            if seguimiento.completado == False:

                seguimientos_pendientes += 1

        return {

            "total_animales": total_animales,
            "estados": reporte_estados,
            "solicitudes_activas": solicitudes_activas,
            "seguimientos_pendientes": seguimientos_pendientes

        }
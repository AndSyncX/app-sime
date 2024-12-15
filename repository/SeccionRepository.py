from util.ConexionBD  import ConexionBD

class SeccionRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarSeccion(self):
        cursor = self.conexion.cursor()
        cursor.callproc('listarSeccion')
        for result in cursor.stored_results():
            return result.fetchall()
        return []
    
    def buscarSeccionID(self, idseccion):
        cursor = self.conexion.cursor()
        cursor.callproc('listarSeccionxId', [idseccion])
        for result in cursor.stored_results():
            return result.fetchone()
        return []
    
    def insertarSeccion(self, seccion):
        cursor = self.conexion.cursor()
        cursor.callproc('insertarSeccion', (
            seccion.id_docente,
            seccion.id_horario,
            seccion.id_curso,
            seccion.nom_seccion,
            seccion.capacidad
        ))
        self.conexion.commit()
        cursor.close()
    
    def actualizarSeccion(self, seccion):
        cursor = self.conexion.cursor()
        cursor.callproc('actualizarSeccion', (
            seccion.id_docente,
            seccion.id_horario,
            seccion.id_curso,
            seccion.nom_seccion,
            seccion.capacidad,
            seccion.id_seccion
        ))
        self.conexion.commit()
        cursor.close()
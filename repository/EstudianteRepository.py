from util.ConexionBD  import ConexionBD

class EstudianteRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    #Listar Estudiante
    def listarEstudiante(self):
        cursor = self.conexion.cursor()
        cursor.callproc('listarEstudiante')
        for result in cursor.stored_results():
            return result.fetchall()
        return []
    
    #Buscar Estudiante x ID
    def listarEstudiantexId(self, idestudiante):
        cursor = self.conexion.cursor()
        cursor.callproc('listarEstudiantexId', [idestudiante])
        for result in cursor.stored_results():
            return result.fetchone()
        return []
    
    #Insertar Estudiante
    def insertarEstudiante(self, estudiante):
        cursor = self.conexion.cursor()
        cursor.callproc('insertarEstudiante', (
            estudiante.id_persona,
            estudiante.id_carrera))
        self.conexion.commit()
        cursor.close()
    
    #Actualizar Estudiante
    def actualizarEstudiante(self, estudiante):
        cursor = self.conexion.cursor()
        cursor.callproc('actualizarEstudiante', (
            estudiante.id_persona,
            estudiante.id_carrera,
            estudiante.id_estudiante))
        self.conexion.commit()
        cursor.close()
    
    #Listar Estudiante x Persona
    def listarEstudiantePersona(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM vista_estudiante"
        cursor.execute(sql)
        return cursor.fetchall()
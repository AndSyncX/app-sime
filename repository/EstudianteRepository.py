from util.ConexionBD  import ConexionBD

class EstudianteRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarEstudiante(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Estudiante"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarEstudianteID(self, idestudiante):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Estudiante WHERE ID_Estudiante = '{}'".format(idestudiante)
        cursor.execute(sql)
        return cursor.fetchone()
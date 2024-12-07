from util.ConexionBD  import ConexionBD

class MatriculaRepository:
    def __init__(self):
        self.conexion = ConexionBD.getConexion()

    def listarMatricula(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Matricula"
        cursor.execute(sql)
        return cursor.fetchall()
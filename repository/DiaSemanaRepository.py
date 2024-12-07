from util.ConexionBD  import ConexionBD

class DiaSemanaRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarDiaSemana(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM diasemana"
        cursor.execute(sql)
        return cursor.fetchall()
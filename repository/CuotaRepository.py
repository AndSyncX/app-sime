from util.ConexionBD  import ConexionBD

class CuotaRepository():
    def __init__(self):
        self.conexion = ConexionBD.getConexion()

    def listarCuota(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Cuota"
        cursor.execute(sql)
        return cursor.fetchall()
    
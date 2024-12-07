from util.ConexionBD  import ConexionBD

class DetalleRepository:
    def __init__(self):
        self.conexion = ConexionBD.getConexion()

    def listarDetalle(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Detalle"
        cursor.execute(sql)
        return cursor.fetchall()
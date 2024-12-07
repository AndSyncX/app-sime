from util.ConexionBD import ConexionBD

class ModalidadRepository:
    
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarModalidad(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM modalidad"
        cursor.execute(sql)
        return cursor.fetchall()
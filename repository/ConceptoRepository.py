from util.ConexionBD import ConexionBD

class ConceptoRepository:
    def __init__(self):
        self.conexion = ConexionBD.getConexion()

    def listarConcepto(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Concepto"
        cursor.execute(sql)
        return cursor.fetchall()

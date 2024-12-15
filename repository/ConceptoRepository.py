from util.ConexionBD import ConexionBD

class ConceptoRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarConcepto(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM concepto ORDER BY id_concepto DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarConceptoID(self, idconcepto):
        cursor = self.conexion.cursor()
        sql =  "SELECT * FROM concepto WHERE id_concepto = '{}'".format(idconcepto)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarConcepto(self, concepto):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO concepto (descripcion, monto) VALUES ('{}', '{}')".format(
            concepto.descripcion,
            concepto.monto
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarConcepto(self, concepto):
        cursor = self.conexion.cursor()
        sql = "UPDATE concepto SET descripcion = '{}', monto = '{}' WHERE id_concepto = '{}'".format(
            concepto.descripcion,
            concepto.monto,
            concepto.id_concepto
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
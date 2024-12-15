from util.ConexionBD  import ConexionBD

class CuotaRepository():
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarCuota(self):
        cursor = self.conexion.cursor()
        cursor.callproc('listarCuota')
        for result in cursor.stored_results():
            return result.fetchall()
        return []
    
    def buscarCuotaID(self, idcuota):
        cursor = self.conexion.cursor()
        cursor.callproc('listarCuotaxId', [idcuota])
        for result in cursor.stored_results():
            return result.fetchone()
        return []
    
    def insertarCuota(self, cuota):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO cuota (id_estudiante, id_concepto, id_matricula, fec_pago, monto, estado) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            cuota.id_estudiante,
            cuota.id_concepto,
            cuota.id_matricula,
            cuota.fec_pago,
            cuota.monto,
            cuota.estado
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarCuota(self, cuota):
        cursor = self.conexion.cursor()
        sql = "UPDATE cuota SET id_estudiante = '{}', id_concepto = '{}', id_matricula = '{}', fec_pago = '{}', monto = '{}', estado = '{}' WHERE id_cuota = '{}'".format(
            cuota.id_estudiante,
            cuota.id_concepto,
            cuota.id_matricula,
            cuota.fec_pago,
            cuota.monto,
            cuota.estado,
            cuota.id_cuota
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
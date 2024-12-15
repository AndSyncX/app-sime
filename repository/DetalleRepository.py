from util.ConexionBD  import ConexionBD

class DetalleRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarDetalle(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Detalle"
        cursor.execute(sql)
        return cursor.fetchall()

    def buscarDetalleID(self, iddetalle):
        cursor = self.conexion.cursor()
        cursor.callproc('listarDetallexId', [iddetalle])
        for result in cursor.stored_results():
            return result.fetchone()
        return []
    
    def insertarDetalle(self, detalle):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO detalle (id_estudiante, id_concepto, id_matricula, fec_pago, monto, estado) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            detalle.id_estudiante,
            detalle.id_concepto,
            detalle.id_matricula,
            detalle.fec_pago,
            detalle.monto,
            detalle.estado
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarDetalle(self, detalle):
        cursor = self.conexion.cursor()
        sql = "UPDATE detalle SET id_estudiante = '{}', id_concepto = '{}', id_matricula = '{}', fec_pago = '{}', monto = '{}', estado = '{}' WHERE id_detalle = '{}'".format(
            detalle.id_estudiante,
            detalle.id_concepto,
            detalle.id_matricula,
            detalle.fec_pago,
            detalle.monto,
            detalle.estado,
            detalle.id_detalle
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
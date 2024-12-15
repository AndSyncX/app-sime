from util.ConexionBD  import ConexionBD

class MatriculaRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarMatricula(self):
        cursor = self.conexion.cursor()
        cursor.callproc('listarMatricula')
        for result in cursor.stored_results():
            return result.fetchall()
        return []

    def buscarMatriculaID(self, idmatricula):
        cursor = self.conexion.cursor()
        cursor.callproc('listarMatriculaxId', [idmatricula])
        for result in cursor.stored_results():
            return result.fetchone()
        return []
    
    def insertarMatricula(self, matricula):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO matricula (id_seccion, id_estudiante, fec_matricula, estado, periodo) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            matricula.id_seccion,
            matricula.id_estudiante,
            matricula.fec_matricula,
            matricula.estado,
            matricula.periodo
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarMatricula(self, matricula):
        cursor = self.conexion.cursor()
        sql = "UPDATE matricula SET id_seccion = '{}', id_estudiante = '{}', fec_matricula = '{}', estado = '{}', periodo = '{}' WHERE id_matricula = '{}'".format(
            matricula.id_seccion,
            matricula.id_estudiante,
            matricula.fec_matricula,
            matricula.estado,
            matricula.periodo,
            matricula.id_matricula
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
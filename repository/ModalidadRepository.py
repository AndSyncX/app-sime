from util.ConexionBD import ConexionBD

class ModalidadRepository:
    
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarModalidad(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM modalidad ORDER BY id_modalidad DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarModalidadID(self, idmodalidad):
        cursor = self.conexion.cursor()
        sql =  "SELECT * FROM modalidad WHERE id_modalidad = '{}'".format(idmodalidad)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarModalidad(self, modalidad):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO modalidad (descripcion) VALUES ('{}')".format(
            modalidad.descripcion,
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarModalidad(self, modalidad):
        cursor = self.conexion.cursor()
        sql = "UPDATE modalidad SET descripcion = '{}' WHERE id_modalidad = '{}'".format(
            modalidad.descripcion,
            modalidad.id_modalidad
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
from util.ConexionBD import ConexionBD

class CarreraRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarCarrera(self):
        cursor = self.conexion.cursor()
        cursor.callproc('listarCarrera')
        for result in cursor.stored_results():
            return result.fetchall()
        return []
    
    def buscarCarreraID(self, idcarrera):
        cursor = self.conexion.cursor()
        sql = "SELECT c.id_carrera, c.nom_carrera, c.creditos_total, c.duracion, m.descripcion FROM carrera c INNER JOIN modalidad m ON c.id_modalidad = m.id_modalidad WHERE id_carrera = '{}' ORDER BY id_carrera DESC".format(idcarrera)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarCarrera(self, carrera):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO carrera(nom_carrera, creditos_total, duracion, id_modalidad) VALUES ('{}', '{}', '{}', '{}')".format(
            carrera.nom_carrera,
            carrera.creditos_total,
            carrera.duracion,
            carrera.id_modalidad
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
        
    def actualizarCarrera(self, carrera):
        cursor = self.conexion.cursor()
        sql = "UPDATE carrera SET nom_carrera = '{}', creditos_total = '{}', duracion = '{}', id_modalidad = '{}' WHERE id_carrera = '{}'".format(
            carrera.nom_carrera,
            carrera.creditos_total,
            carrera.duracion,
            carrera.id_modalidad,
            carrera.id_carrera
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
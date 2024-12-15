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
        cursor.callproc('listarCarreraxId', [idcarrera])
        for result in cursor.stored_results():
            return result.fetchone()
        return []
    
    def insertarCarrera(self, carrera):
        cursor = self.conexion.cursor()
        cursor.callproc("insertarCarrera", (
            carrera.nom_carrera,
            carrera.creditos_total,
            carrera.duracion,
            carrera.id_modalidad
        ))
        self.conexion.commit()
        cursor.close()
        
    def actualizarCarrera(self, carrera):
        cursor = self.conexion.cursor()
        cursor.callproc("actualizarCarrera", (
            carrera.nom_carrera,
            carrera.creditos_total,
            carrera.duracion,
            carrera.id_modalidad,
            carrera.id_carrera
        ))
        self.conexion.commit()
        cursor.close()
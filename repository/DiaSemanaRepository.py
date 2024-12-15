from util.ConexionBD  import ConexionBD

class DiaSemanaRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarDiaSemana(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM diasemana ORDER BY id_dia_semana DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarDiaSemanaID(self, id_diasemana):
        cursor = self.conexion.cursor()
        sql =  "SELECT * FROM diasemana WHERE id_dia_semana = '{}'".format(id_diasemana)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarDiaSemana(self, diasemana):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO diasemana (descripcion) VALUES ('{}')".format(
            diasemana.descripcion,
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarDiaSemana(self, diasemana):
        cursor = self.conexion.cursor()
        sql = "UPDATE diasemana SET descripcion = '{}' WHERE id_dia_semana = '{}'".format(
            diasemana.descripcion,
            diasemana.id_dia_semana
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
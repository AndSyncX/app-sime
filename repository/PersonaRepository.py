from util.ConexionBD  import ConexionBD

class PersonaRepository:
    def __init__(self):
        self.conexion = ConexionBD.getConexion()

    def listarPersona(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Persona"
        cursor.execute(sql)
        return cursor.fetchall()
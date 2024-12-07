from util.ConexionBD  import ConexionBD

class DocenteRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarDocente(self):
        cursor = self.conexion.cursor()
        sql = "SELECT  d.id_docente, p.ape_paterno, p.ape_materno, p.nom1, p.nom2, p.dni, p.departamento, p.provincia, p.distrito, p.direccion, p.celular, p.correo, p.fec_nacimiento, p.estado_civil, p.sexo FROM docente d INNER JOIN persona p ON d.id_persona = p.id_persona ORDER BY id_docente DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarDocenteID(self, iddocente):
        cursor = self.conexion.cursor()
        sql = "SELECT  d.id_docente, p.ape_paterno, p.ape_materno, p.nom1, p.nom2, p.dni, p.departamento, p.provincia, p.distrito, p.direccion, p.celular, p.correo, p.fec_nacimiento, p.estado_civil, p.sexo FROM docente d INNER JOIN persona p ON d.id_persona = p.id_persona WHERE d.id_docente '{}' ORDER BY id_docente DESC".format(iddocente)
        cursor.execute(sql)
        return cursor.fetchone()
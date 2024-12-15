from util.ConexionBD  import ConexionBD

class DocenteRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarDocente(self):
        cursor = self.conexion.cursor()
        sql = "SELECT  d.id_docente, p.id_persona, p.ape_paterno, p.ape_materno, p.nom1, p.nom2, p.dni, p.departamento, p.provincia, p.distrito, p.direccion, p.celular, p.correo, p.fec_nacimiento, p.sexo, d.especialidad FROM docente d INNER JOIN persona p ON d.id_persona = p.id_persona ORDER BY id_docente DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarDocenteID(self, iddocente):
        cursor = self.conexion.cursor()
        sql = "SELECT d.id_docente, p.id_persona, p.ape_paterno, p.ape_materno, p.nom1, p.nom2, p.dni, p.departamento, p.provincia, p.distrito, p.direccion, p.celular, p.correo, p.fec_nacimiento, p.sexo, d.especialidad FROM docente d INNER JOIN persona p ON d.id_persona = p.id_persona WHERE d.id_docente = %s ORDER BY id_docente DESC"
        cursor.execute(sql, (iddocente,))
        return cursor.fetchone()
    
    def insertarDocente(self, docente):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO docente(especialidad, id_persona) VALUES ('{}', '{}')".format(
            docente.especialidad,
            docente.id_persona
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarDocente(self, docente):
        cursor = self.conexion.cursor()
        sql = "UPDATE docente SET especialidad = '{}', id_persona = '{}' WHERE id_docente = '{}'".format(
            docente.especialidad,
            docente.id_persona,
            docente.id_docente
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()   

    def listarDocentePersona(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM vista_docente"
        cursor.execute(sql)
        return cursor.fetchall()
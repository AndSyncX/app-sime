from util.ConexionBD  import ConexionBD

class PersonaRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarPersona(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM persona"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarPersonaxID(self, idpersona):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM persona WHERE id_persona = '{}'".format(idpersona)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarPersona(self, persona):
        cursor = self.conexion.cursor()
        id_generado = 0
        result = cursor.callproc('insertarPersona', (
            persona.ape_paterno,
            persona.ape_materno,
            persona.nom1,
            persona.nom2,
            persona.dni,
            persona.departamento,
            persona.provincia,
            persona.distrito,
            persona.direccion,
            persona.celular,
            persona.correo,
            persona.fec_nacimiento,
            persona.sexo,
            id_generado
        ))
        self.conexion.commit()
        # El último valor es el ID generado
        id_generado = result[-1]  
        cursor.close()
        return id_generado
    
    def actualizarPersona(self, persona):
        cursor = self.conexion.cursor()
        cursor.callproc('actualizarPersona', (
            persona.ape_paterno,
            persona.ape_materno,
            persona.nom1,
            persona.nom2,
            persona.dni,
            persona.departamento,
            persona.provincia,
            persona.distrito,
            persona.direccion,
            persona.celular,
            persona.correo,
            persona.fec_nacimiento,
            persona.sexo,
            persona.id_persona
        ))
        self.conexion.commit()
        cursor.close()

    def verificarPersona(self, dni):
        cursor = self.conexion.cursor()
        sql = "SELECT COUNT(*) FROM persona WHERE dni = '{}'".format(dni)
        cursor.execute(sql)
        existe = cursor.fetchone()[0] > 0
        cursor.close()
        return existe
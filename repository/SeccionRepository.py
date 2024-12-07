from util.ConexionBD  import ConexionBD

class SeccionRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarSeccion(self):
        cursor = self.conexion.cursor()
        sql = "SELECT s.id_seccion, p.ape_paterno AS nombre_docente, h.hora_inicio, c.nom_curso, s.nom_seccion, s.capacidad FROM seccion s INNER JOIN docente d ON d.id_docente = s.id_docente INNER JOIN persona p ON p.id_persona = d.id_persona INNER JOIN horario h ON h.id_horario = s.id_horario INNER JOIN curso c ON c.id_curso = s.id_curso ORDER BY id_seccion DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarSeccionID(self, idseccion):
        cursor = self.conexion.cursor()
        sql = "SELECT s.id_seccion, p.ape_paterno, h.hora_inicio, c.nom_curso, s.nom_seccion, s.capacidad FROM seccion s INNER JOIN docente d ON d.id_docente = s.id_docente INNER JOIN persona p ON p.id_persona = d.id_persona INNER JOIN horario h ON h.id_horario = s.id_horario INNER JOIN curso c ON c.id_curso = s.id_curso  WHERE id_seccion = '{}' ORDER BY id_seccion DESC".format(idseccion)
        cursor.execute(sql)
        return cursor.fetchone()
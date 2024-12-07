from util.ConexionBD  import ConexionBD

class CursoRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarCurso(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM curso ORDER BY id_curso DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarCursoID(self, idcurso):
        cursor = self.conexion.cursor()
        sql =  "SELECT * FROM curso WHERE id_curso = '{}'".format(idcurso)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarCurso(self, curso):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO curso (nom_curso, creditos) VALUES ('{}', '{}')".format(
            curso.nom_curso,
            curso.creditos
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarCurso(self, curso):
        cursor = self.conexion.cursor()
        sql = "UPDATE curso SET nom_Curso = '{}', creditos = '{}' WHERE id_curso = '{}'".format(
            curso.nom_curso,
            curso.creditos,
            curso.id_curso,
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
from util.ConexionBD  import ConexionBD

class HorarioRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarHorario(self):
        cursor = self.conexion.cursor()
        sql = "SELECT h.id_horario, h.hora_inicio, h.hora_fin, d.descripcion FROM horario h INNER JOIN diaSemana d ON h.id_dia_semana = d.id_dia_semana ORDER BY id_horario DESC"
        cursor.execute(sql)
        return cursor.fetchall()

    def buscarHorarioID(self, idhorario):
        cursor = self.conexion.cursor()
        sql = "SELECT h.id_horario, h.hora_inicio, h.hora_fin, d.descripcion FROM horario h INNER JOIN diaSemana d ON h.id_dia_semana = d.id_dia_semana WHERE id_horario = '{}' ORDER BY id_horario DESC".format(idhorario)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarHorario(self, horario):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO horario (hora_inicio, hora_fin, id_dia_semana) VALUES ('{}', '{}', '{}')".format(
            horario.hora_inicio,
            horario.hora_fin,
            horario.id_dia_semana
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarHorario(self, horario):
        cursor = self.conexion.cursor()
        sql = "UPDATE horario SET hora_inicio = '{}', hora_fin = '{}', id_dia_semana = '{}' WHERE id_horario = '{}'".format(
            horario.hora_inicio,
            horario.hora_fin,
            horario.id_dia_semana,
            horario.id_horario
        )
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
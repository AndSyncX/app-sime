from util.ConexionBD  import ConexionBD

class HorarioRepository:
    def __init__(self):
        self.conexion = ConexionBD().getConexion()

    def listarHorario(self):
        cursor = self.conexion.cursor()
        cursor.callproc('listarHorario')
        for result in cursor.stored_results():
            return result.fetchall()
        return []

    def buscarHorarioID(self, idhorario):
        cursor = self.conexion.cursor()
        cursor.callproc('listarHorarioxId', [idhorario])
        for result in cursor.stored_results():
            return result.fetchone()
        return []
    
    def insertarHorario(self, horario):
        cursor = self.conexion.cursor()
        cursor.callproc('insertarHorario', (
            horario.hora_inicio,
            horario.hora_fin,
            horario.id_dia_semana))
        self.conexion.commit()
        cursor.close()
    
    def actualizarHorario(self, horario):
        cursor = self.conexion.cursor()
        cursor.callproc('actualizarHorario', (
            horario.hora_inicio,
            horario.hora_fin,
            horario.id_dia_semana,
            horario.id_horario))
        self.conexion.commit()
        cursor.close()
        
    def listarHorarioDiasemana(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM vista_horario"
        cursor.execute(sql)
        return cursor.fetchall()
import mysql.connector

class ConexionBD:

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            database='bdsime',
            user='root',
            password='1234'
        )
        
    def getConexion(self):
        return self.conexion
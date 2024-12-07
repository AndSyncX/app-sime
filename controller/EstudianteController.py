from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from repository.EstudianteRepository import EstudianteRepository
from model.Estudiante import Estudiante

class EstudianteController():
    
    def __init__(self):
        self.objEstudianteRepository = EstudianteRepository()
        self.ventana = uic.loadUi("view/frmEstudiante.ui")
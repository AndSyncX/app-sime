from PyQt5 import QtWidgets, uic
from controller.CarreraController import CarreraController
from controller.ConceptoController import ConceptoController
from controller.CuotaController import CuotaController
from controller.CursoController import CursoController
from controller.DetalleContoller import DetalleController
from controller.DocenteController import DocenteController
from controller.EstudianteController import EstudianteController
from controller.HorarioController import HorarioController
from controller.MatriculaController import MatriculaController
from controller.SeccionController import SeccionController
from controller.ModalidadController import ModalidadController
from controller.DiaSemanaController import DiaSemanaController

class PrincipalController():
    
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/main.ui")
        self.ventana.show()
        self.ventana.btnCarrera.clicked.connect(self.btnCarreraClick)
        self.ventana.btnConcepto.clicked.connect(self.btnConceptoClick)
        self.ventana.btnCuota.clicked.connect(self.btnCuotaClick)
        self.ventana.btnCurso.clicked.connect(self.btnCursoClick)
        self.ventana.btnDetalle.clicked.connect(self.btnDetalleClick)
        self.ventana.btnDocente.clicked.connect(self.btnDocenteClick)
        self.ventana.btnEstudiante.clicked.connect(self.btnEstudianteClick)
        self.ventana.btnHorario.clicked.connect(self.btnHorarioClick)
        self.ventana.btnMatricula.clicked.connect(self.btnMatriculaClick)
        self.ventana.btnSeccion.clicked.connect(self.btnSeccionClick)
        self.ventana.btnModalidad.clicked.connect(self.btnModalidadClick)
        self.ventana.btnDiaSemana.clicked.connect(self.btnDiaSemanaClick)
        app.exec()
    
    def btnCarreraClick(self):
        self.frmCarrera = CarreraController()
        self.frmCarrera.ventana.show()
    
    def btnConceptoClick(self):
        self.frmConcepto = ConceptoController()
        self.frmConcepto.ventana.show()
    
    def btnEstudianteClick(self):
        self.frmEstudiante = EstudianteController()
        self.frmEstudiante.ventana.show()
        
    def btnCursoClick(self):
        self.frmCurso = CursoController()
        self.frmCurso.ventana.show()

    def btnHorarioClick(self):
        self.frmHorario = HorarioController()
        self.frmHorario.ventana.show()
    
    def btnSeccionClick(self):
        self.frmSeccion = SeccionController()
        self.frmSeccion.ventana.show()
    
    def btnDocenteClick(self):
        self.frmDocente = DocenteController()
        self.frmDocente.ventana.show()

    def btnModalidadClick(self):
        self.frmModalidad = ModalidadController()
        self.frmModalidad.ventana.show()
    
    def btnDiaSemanaClick(self):
        self.frmDiaSemana = DiaSemanaController()
        self.frmDiaSemana.ventana.show()

    def btnMatriculaClick(self):
        self.frmMatricula = MatriculaController()
        self.frmMatricula.ventana.show()
    
    def btnCuotaClick(self):
        self.frmCuota = CuotaController()
        self.frmCuota.ventana.show()
    
    def btnDetalleClick(self):
        self.frmDetalle = DetalleController()
        self.frmDetalle.ventana.show()
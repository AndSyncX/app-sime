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
from controller.PersonaController import PersonaController
from controller.SeccionController import SeccionController

class PrincipalController():
    
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/main.ui")
        self.ventana.show()
        self.ventana.actionCarrera.triggered.connect(self.actionCarreraClick)
        #self.ventana.actionConcepto.triggered.connect(self.actionConceptoClick)
        #self.ventana.actionCuota.triggered.connect(self.actionCuotaClick)
        self.ventana.actionCurso.triggered.connect(self.actionCursoClick)
        #self.ventana.actionDetalle.triggered.connect(self.actionDetalleClick)
        #self.ventana.actionDocente.triggered.connect(self.actionDocenteClick)
        self.ventana.actionEstudiante.triggered.connect(self.actionEstudianteClick)
        self.ventana.actionHorario.triggered.connect(self.actionHorarioClick)
        #self.ventana.actionMatricula.triggered.connect(self.actionMatriculaClick)
        #self.ventana.actionPersona.triggered.connect(self.actionPersonaClick)
        self.ventana.actionSeccion.triggered.connect(self.actionSeccionClick)
        app.exec()
    
    def actionCarreraClick(self):
        self.frmCarrera = CarreraController()
        self.frmCarrera.ventana.show()
    
    def actionConceptoClick(self):
        self.frmConcepto = ConceptoController()
        self.frmConcepto.ventana.show()
    
    def actionEstudianteClick(self):
        self.frmEstudiante = EstudianteController()
        self.frmEstudiante.ventana.show()
        
    def actionCursoClick(self):
        self.frmCurso = CursoController()
        self.frmCurso.ventana.show()

    def actionHorarioClick(self):
        self.frmHorario = HorarioController()
        self.frmHorario.ventana.show()
    
    def actionSeccionClick(self):
        self.frmSeccion = SeccionController()
        self.frmSeccion.ventana.show()
    
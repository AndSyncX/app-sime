from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.MatriculaRepository import MatriculaRepository
from repository.SeccionRepository import SeccionRepository
from repository.EstudianteRepository import EstudianteRepository
from model.Matricula import Matricula

class MatriculaController():
    
    def __init__(self) -> None:
        self.objMatriculaRepository = MatriculaRepository()
        self.objSeccionRepository = SeccionRepository()
        self.objEstudianteRepository = EstudianteRepository()
        self.ventana = uic.loadUi("view/frmMatricula.ui")
        self.ventana.tblMatricula.cellClicked.connect(self.tblMatriculaCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarMatricula()
        self.listarSeccion()
        self.listarEstudiante()

    def limpiarDatos(self):
        self.ventana.txtIdMatricula.clear()
        self.ventana.cboSeccion.setCurrentIndex(0)
        self.ventana.cboEstudiante.setCurrentIndex(0)
        self.ventana.txtFecMatricula.clear()
        self.ventana.txtEstado.clear()
        self.ventana.txtPeriodo.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idmatricula = self.ventana.txtIdMatricula.text()
        seccion = self.ventana.cboSeccion.currentData()
        estudiante = self.ventana.cboEstudiante.currentData()
        fecha_matricula = self.ventana.txtFecMatricula.text()
        estado = self.ventana.txtEstado.text()
        periodo = self.ventana.txtPeriodo.text()

        newMatricula = Matricula(idmatricula, seccion, estudiante, fecha_matricula, estado, periodo)
        if estado == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objMatriculaRepository.insertarMatricula(newMatricula)
            self.listarMatricula()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Alumno matricula exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        idmatricula = self.ventana.txtIdMatricula.text()
        seccion = self.ventana.cboSeccion.currentData()
        estudiante = self.ventana.cboEstudiante.currentData()
        fecha_matricula = self.ventana.txtFecMatricula.text()
        estado = self.ventana.txtEstado.text()
        periodo = self.ventana.txtPeriodo.text()

        newMatricula = Matricula(idmatricula, seccion, estudiante, fecha_matricula, estado, periodo)
        if idmatricula == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objMatriculaRepository.actualizarMatricula(newMatricula)
            self.limpiarDatos()
            self.listarMatricula()
            QMessageBox.information(self.ventana, "Éxito", "Matricula actualizada exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()
    
    def tblMatriculaCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idmatricula = self.ventana.tblMatricula.item(fila, 0).text()
        self.ventana.txtIdMatricula.setText(idmatricula)
        objMatricula = self.objMatriculaRepository.buscarMatriculaID(idmatricula)
        self.ventana.cboSeccion.setCurrentText(str(objMatricula[1]))
        self.ventana.cboEstudiante.setCurrentText(str(objMatricula[2]))
        self.ventana.txtFecMatricula.setText(str(objMatricula[3]))
        self.ventana.txtEstado.setText(str(objMatricula[4]))
        self.ventana.txtPeriodo.setText(str(objMatricula[5]))

    def listarMatricula(self):
        self.ventana.txtIdMatricula.setEnabled(False)
        listaMatricula = self.objMatriculaRepository.listarMatricula()
        cantidad = len(listaMatricula)
        self.ventana.tblMatricula.setRowCount(cantidad)
        fila = 0
        for matricula in listaMatricula:
            self.ventana.tblMatricula.setItem(fila, 0, QTableWidgetItem(str(matricula[0])))
            self.ventana.tblMatricula.setItem(fila, 1, QTableWidgetItem(str(matricula[1])))
            self.ventana.tblMatricula.setItem(fila, 2, QTableWidgetItem(str(matricula[2])))
            self.ventana.tblMatricula.setItem(fila, 3, QTableWidgetItem(str(matricula[3])))
            self.ventana.tblMatricula.setItem(fila, 4, QTableWidgetItem(str(matricula[4])))
            self.ventana.tblMatricula.setItem(fila, 5, QTableWidgetItem(str(matricula[5])))
            fila += 1
    
    def listarSeccion(self):
        listaSeccion = self.objSeccionRepository.listarSeccion()
        for seccion in listaSeccion:
            self.ventana.cboSeccion.addItem(
                seccion[4],
                seccion[0]
            )

    def listarEstudiante(self):
        listaEstudiante = self.objEstudianteRepository.listarEstudiantePersona()
        for estudiante in listaEstudiante:
            self.ventana.cboEstudiante.addItem(
                estudiante[1],
                estudiante[0]
            )
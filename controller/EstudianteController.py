from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.EstudianteRepository import EstudianteRepository
from repository.PersonaRepository import PersonaRepository
from repository.CarreraRepository import CarreraRepository
from model.Estudiante import Estudiante
from model.Persona import Persona

class EstudianteController():
    
    def __init__(self):
        self.objEstudianteRepository = EstudianteRepository()
        self.objPersonaRepository = PersonaRepository()
        self.objCarreraRepository = CarreraRepository()
        self.ventana = uic.loadUi("view/frmEstudiante.ui")
        self.ventana.tblEstudiante.cellClicked.connect(self.tblEstudianteCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarEstudiante()
        self.listarCarrera()

    def limpiarDatos(self):
        self.ventana.txtIdEstudiante.clear()
        self.ventana.txtIdPersona.clear()
        self.ventana.txtApepaterno.clear()
        self.ventana.txtApematerno.clear()
        self.ventana.txtNom1.clear()
        self.ventana.txtNom2.clear()
        self.ventana.txtDNI.clear()
        self.ventana.txtDepartamento.clear()
        self.ventana.txtProvincia.clear()
        self.ventana.txtDistrito.clear()
        self.ventana.txtDireccion.clear()
        self.ventana.txtCelular.clear()
        self.ventana.txtCorreo.clear()
        self.ventana.txtFecnacimiento.clear()

        self.ventana.rbMasculino.setAutoExclusive(False)
        self.ventana.rdFemenino.setAutoExclusive(False)
        self.ventana.rbMasculino.setChecked(False)
        self.ventana.rdFemenino.setChecked(False)
        self.ventana.rbMasculino.setAutoExclusive(True)
        self.ventana.rdFemenino.setAutoExclusive(True)
        
        self.ventana.cboCarrera.setCurrentIndex(0)
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idEstudiante = self.ventana.txtIdEstudiante.text()
        apepaterno = self.ventana.txtApepaterno.text()
        apematerno = self.ventana.txtApematerno.text()
        nom1 = self.ventana.txtNom1.text()
        nom2 = self.ventana.txtNom2.text()
        dni = self.ventana.txtDNI.text()
        departamento = self.ventana.txtDepartamento.text()
        provincia = self.ventana.txtProvincia.text()
        distrito = self.ventana.txtDistrito.text()
        direccion = self.ventana.txtDireccion.text()
        celular = self.ventana.txtCelular.text()
        correo = self.ventana.txtCorreo.text()
        fecnacimiento = self.ventana.txtFecnacimiento.text()
        carrera = self.ventana.cboCarrera.currentData()
        sexo = ""
        
        if self.ventana.rbMasculino.isChecked():
            sexo = "M"
        elif self.ventana.rdFemenino.isChecked():
            sexo = "F"
        
        newPersona = Persona(None, apepaterno, apematerno, nom1, nom2, dni, departamento, provincia, distrito, direccion, celular, correo, fecnacimiento, sexo)
        
        if apepaterno == "" or apematerno == "":
            QMessageBox.information(self.ventana, "Error", "Campos Incompletos", QMessageBox.Ok)
        else:
            if not self.objPersonaRepository.verificarPersona(dni):
                idPersona = self.objPersonaRepository.insertarPersona(newPersona)

            newEstudiante = Estudiante(
                idPersona, apepaterno, apematerno, nom1, nom2, dni, departamento,
                provincia, distrito, direccion, celular, correo, fecnacimiento, sexo,
                idEstudiante, carrera)
            self.objEstudianteRepository.insertarEstudiante(newEstudiante)
            self.listarEstudiante()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Persona Registrado Exitosamente", QMessageBox. Ok)

    def btnActualizarClick(self):
        idEstudiante = self.ventana.txtIdEstudiante.text()
        idPersona = self.ventana.txtIdPersona.text()
        apepaterno = self.ventana.txtApepaterno.text()
        apematerno = self.ventana.txtApematerno.text()
        nom1 = self.ventana.txtNom1.text()
        nom2 = self.ventana.txtNom2.text()
        dni = self.ventana.txtDNI.text()
        departamento = self.ventana.txtDepartamento.text()
        provincia = self.ventana.txtProvincia.text()
        distrito = self.ventana.txtDistrito.text()
        direccion = self.ventana.txtDireccion.text()
        celular = self.ventana.txtCelular.text()
        correo = self.ventana.txtCorreo.text()
        fecnacimiento = self.ventana.txtFecnacimiento.text()
        carrera = self.ventana.cboCarrera.currentData()
        sexo = ""

        if self.ventana.rbMasculino.isChecked():
            sexo = "M"
        elif self.ventana.rdFemenino.isChecked():
            sexo = "F"

        newPersona = Persona(idPersona, apepaterno, apematerno, nom1, nom2, dni, departamento, provincia, distrito, direccion, celular, correo, fecnacimiento, sexo)
        newEstudiante = Estudiante(idPersona, apepaterno, apematerno, nom1, nom2, dni, departamento, provincia, distrito, direccion, celular, correo, fecnacimiento, sexo, idEstudiante, carrera)
        
        if idPersona == "":
            QMessageBox.information(self.ventana, "Error", "Campos Incompletos", QMessageBox.Ok)
        else:
            self.objEstudianteRepository.actualizarEstudiante(newEstudiante)
            self.objPersonaRepository.actualizarPersona(newPersona)
            self.ventana.btnRegistrar.setEnabled(True)
            QMessageBox.information(self.ventana, "Éxito", "Estudiante actualizada exitosamente", QMessageBox.Ok)
            self.limpiarDatos()
            self.listarEstudiante()
            
    def btnLimpiarClick(self):
        self.limpiarDatos()

    def tblEstudianteCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idEstudiante = self.ventana.tblEstudiante.item(fila, 0).text()
        self.ventana.txtIdEstudiante.setText(idEstudiante)
        objEstudiante = self.objEstudianteRepository.listarEstudiantexId(idEstudiante)
        self.ventana.txtIdPersona.setText(str(objEstudiante[1]))
        self.ventana.txtApepaterno.setText(objEstudiante[2])
        self.ventana.txtApematerno.setText(objEstudiante[3])
        self.ventana.txtNom1.setText(objEstudiante[4])
        self.ventana.txtNom2.setText(objEstudiante[5])
        self.ventana.txtDNI.setText(objEstudiante[6])
        self.ventana.txtDepartamento.setText(objEstudiante[7])
        self.ventana.txtProvincia.setText(objEstudiante[8])
        self.ventana.txtDistrito.setText(objEstudiante[9])
        self.ventana.txtDireccion.setText(objEstudiante[10])
        self.ventana.txtCelular.setText(str(objEstudiante[11]))
        self.ventana.txtCorreo.setText(str(objEstudiante[12]))
        self.ventana.txtFecnacimiento.setText(str(objEstudiante[13]))
        
        if objEstudiante[14] == "M":
            self.ventana.rbMasculino.setChecked(True)
        else:
            self.ventana.rdFemenino.setChecked(True)
        
        self.ventana.cboCarrera.setCurrentText(objEstudiante[15])
        
    def listarEstudiante(self):
        self.ventana.txtIdEstudiante.setEnabled(False)
        self.ventana.txtIdPersona.setEnabled(False)
        listaEstdiante = self.objEstudianteRepository.listarEstudiante()
        cantidad = len(listaEstdiante)
        self.ventana.tblEstudiante.setRowCount(cantidad)
        fila = 0
        for estudiante in listaEstdiante:
            self.ventana.tblEstudiante.setItem(fila, 0, QTableWidgetItem(str(estudiante[0])))
            self.ventana.tblEstudiante.setItem(fila, 1, QTableWidgetItem(str(estudiante[1])))
            self.ventana.tblEstudiante.setItem(fila, 2, QTableWidgetItem(estudiante[2]))
            self.ventana.tblEstudiante.setItem(fila, 3, QTableWidgetItem(estudiante[3]))
            self.ventana.tblEstudiante.setItem(fila, 4, QTableWidgetItem(estudiante[4]))
            self.ventana.tblEstudiante.setItem(fila, 5, QTableWidgetItem(str(estudiante[5])))
            self.ventana.tblEstudiante.setItem(fila, 6, QTableWidgetItem(estudiante[6]))
            self.ventana.tblEstudiante.setItem(fila, 7, QTableWidgetItem(estudiante[7]))
            self.ventana.tblEstudiante.setItem(fila, 8, QTableWidgetItem(estudiante[8]))
            self.ventana.tblEstudiante.setItem(fila, 9, QTableWidgetItem(estudiante[9]))
            self.ventana.tblEstudiante.setItem(fila, 10, QTableWidgetItem(str(estudiante[10])))
            self.ventana.tblEstudiante.setItem(fila, 11, QTableWidgetItem(str(estudiante[11])))
            self.ventana.tblEstudiante.setItem(fila, 12, QTableWidgetItem(str(estudiante[12])))
            self.ventana.tblEstudiante.setItem(fila, 13, QTableWidgetItem(str(estudiante[13])))
            self.ventana.tblEstudiante.setItem(fila, 14, QTableWidgetItem(str(estudiante[14])))
            self.ventana.tblEstudiante.setItem(fila, 15, QTableWidgetItem(str(estudiante[15])))
            fila += 1

    def listarCarrera(self):
        listaCarrera = self.objCarreraRepository.listarCarrera()
        for carrera in listaCarrera:
            self.ventana.cboCarrera.addItem(
                carrera[1],
                carrera[0]
            )
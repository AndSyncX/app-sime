from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.DocenteRepository import DocenteRepository
from repository.PersonaRepository import PersonaRepository
from model.Docente import Docente
from model.Persona import Persona

class DocenteController():
    
    def __init__(self):
        self.objDocenteRepository = DocenteRepository()
        self.objPersonaRepository = PersonaRepository()
        self.ventana = uic.loadUi("view/frmDocente.ui")
        self.ventana.tblDocente.cellClicked.connect(self.tblDocenteCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarDocente()

    def limpiarDatos(self):
        self.ventana.txtIdDocente.clear()
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
        
        self.ventana.txtEspecialidad.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idDocente = self.ventana.txtIdDocente.text()
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
        sexo = "-"
        
        if self.ventana.rbMasculino.isChecked():
            sexo = "M"
        elif self.ventana.rdFemenino.isChecked():
            sexo = "F"

        especialidad = self.ventana.txtEspecialidad.text()

        newPersona = Persona(None, apepaterno, apematerno, nom1, nom2, dni, departamento, provincia, distrito, direccion, celular, correo, fecnacimiento, sexo)

        if apepaterno == "" or apematerno == "":
            QMessageBox.information(self.ventana, "Error", "Campos Incompletos", QMessageBox.Ok)
        else:
            if not self.objPersonaRepository.verificarPersona(dni):
                idPersona = self.objPersonaRepository.insertarPersona(newPersona)

            newDocente = Docente(
                idPersona, apepaterno, apematerno, nom1, nom2, dni, departamento,
                provincia, distrito, direccion, celular, correo, fecnacimiento, sexo,
                idDocente, especialidad
            )
            self.objDocenteRepository.insertarDocente(newDocente)
            
            self.listarDocente()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Persona Registrado Exitosamente", QMessageBox. Ok)

    def btnActualizarClick(self):
        idDocente = self.ventana.txtIdDocente.text()
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
        sexo = "-"
        
        if self.ventana.rbMasculino.isChecked():
            sexo = "M"
        elif self.ventana.rdFemenino.isChecked():
            sexo = "F"

        especialidad = self.ventana.txtEspecialidad.text()

        newPersona = Persona(idPersona, apepaterno, apematerno, nom1, nom2, dni, departamento, provincia, distrito, direccion, celular, correo, fecnacimiento, sexo)
        newDocente = Docente(idPersona, apepaterno, apematerno, nom1, nom2, dni, departamento, provincia, distrito, direccion, celular, correo, fecnacimiento, sexo, idDocente, especialidad)
        if idPersona == "":
            QMessageBox.information(self.ventana, "Error", "Campos Incompletos", QMessageBox.Ok)
        else:
            self.objDocenteRepository.actualizarDocente(newDocente)
            self.objPersonaRepository.actualizarPersona(newPersona)
            self.limpiarDatos()
            self.listarDocente()
            QMessageBox.information(self.ventana, "Éxito", "Estudiante actualizada exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()

    def tblDocenteCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idDocente = self.ventana.tblDocente.item(fila, 0).text()
        self.ventana.txtIdDocente.setText(idDocente)
        objDocente = self.objDocenteRepository.buscarDocenteID(idDocente)
        self.ventana.txtIdPersona.setText(str(objDocente[1]))
        self.ventana.txtApepaterno.setText(objDocente[2])
        self.ventana.txtApematerno.setText(objDocente[3])
        self.ventana.txtNom1.setText(objDocente[4])
        self.ventana.txtNom2.setText(objDocente[5])
        self.ventana.txtDNI.setText(objDocente[6])
        self.ventana.txtDepartamento.setText(objDocente[7])
        self.ventana.txtProvincia.setText(objDocente[8])
        self.ventana.txtDistrito.setText(objDocente[9])
        self.ventana.txtDireccion.setText(str(objDocente[10]))
        self.ventana.txtCelular.setText(str(objDocente[11]))
        self.ventana.txtCorreo.setText(str(objDocente[12]))
        self.ventana.txtFecnacimiento.setText(str(objDocente[13]))

        if objDocente[14] == "M":
            self.ventana.rbMasculino.setChecked(True)
        else:
            self.ventana.rdFemenino.setChecked(True)
        self.ventana.txtEspecialidad.setText(str(objDocente[15]))

    def listarDocente(self):
        self.ventana.txtIdDocente.setEnabled(False)
        self.ventana.txtIdPersona.setEnabled(False)
        listaDocente = self.objDocenteRepository.listarDocente()
        cantidad = len(listaDocente)
        self.ventana.tblDocente.setRowCount(cantidad)
        fila = 0
        for docente in listaDocente:
            self.ventana.tblDocente.setItem(fila, 0, QTableWidgetItem(str(docente[0])))
            self.ventana.tblDocente.setItem(fila, 1, QTableWidgetItem(str(docente[1])))
            self.ventana.tblDocente.setItem(fila, 2, QTableWidgetItem(docente[2]))
            self.ventana.tblDocente.setItem(fila, 3, QTableWidgetItem(docente[3]))
            self.ventana.tblDocente.setItem(fila, 4, QTableWidgetItem(docente[4]))
            self.ventana.tblDocente.setItem(fila, 5, QTableWidgetItem(str(docente[5])))
            self.ventana.tblDocente.setItem(fila, 6, QTableWidgetItem(docente[6]))
            self.ventana.tblDocente.setItem(fila, 7, QTableWidgetItem(docente[7]))
            self.ventana.tblDocente.setItem(fila, 8, QTableWidgetItem(docente[8]))
            self.ventana.tblDocente.setItem(fila, 9, QTableWidgetItem(docente[9]))
            self.ventana.tblDocente.setItem(fila, 10, QTableWidgetItem(str(docente[10])))
            self.ventana.tblDocente.setItem(fila, 11, QTableWidgetItem(str(docente[11])))
            self.ventana.tblDocente.setItem(fila, 12, QTableWidgetItem(str(docente[12])))
            self.ventana.tblDocente.setItem(fila, 13, QTableWidgetItem(str(docente[13])))
            self.ventana.tblDocente.setItem(fila, 14, QTableWidgetItem(str(docente[14])))
            self.ventana.tblDocente.setItem(fila, 15, QTableWidgetItem(str(docente[15])))
            fila += 1


from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.PersonaRepository import PersonaRepository
from model.Persona import Persona

class PersonaController():
    
    def __init__(self) -> None:
        self.objPersonaRepository = PersonaRepository()
        self.ventana = uic.loadUi("view/frmPersona.ui")
        self.ventana.tblPersona.cellClicked.connect(self.tblPersonaCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarPersona()

    def limpiarDatos(self):
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
        self.ventana.rbMasculino.setChecked(False)
        self.ventana.rdFemenino.setChecked(False)
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
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
        newPersona = Persona(idPersona, apepaterno, apematerno, nom1, nom2, dni, departamento, provincia, distrito, direccion, celular, correo, fecnacimiento, sexo)
        if apepaterno == "" or apematerno == "":
            QMessageBox.information(self.ventana, "Error", "Campos Incompletos", QMessageBox.Ok)
        else:
            self.objPersonaRepository.insertarPersona(newPersona)
            self.listarPersona()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Persona Registrado Exitosamente", QMessageBox. Ok)

    def btnActualizarClick(self):
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
        if self.ventana.rbMasculino.isChecked():
            sexo = "M"
        elif self.ventana.rdFemenino.isChecked():
            sexo = "F"
        newPersona = Persona(idPersona, apepaterno, apematerno, nom1, nom2, dni, departamento, provincia, distrito, direccion, celular, correo, fecnacimiento, sexo)
        if idPersona == "":
            QMessageBox.information(self.ventana, "Error", "Campos Incompletos", QMessageBox.Ok)
        else:
            self.objPersonaRepository.actualizarSeccion(newPersona)
            self.limpiarDatos()
            self.listarPersona()
            QMessageBox.information(self.ventana, "Éxito", "Persona actualizada exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()

    def tblPersonaCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idPersona = self.ventana.tblPersona.item(fila, 0).text()
        self.ventana.txtIdPersona.setText(idPersona)
        objPersona = self.objPersonaRepository.buscarPersonaxID(idPersona)
        self.ventana.txtApepaterno.setText(objPersona[1])
        self.ventana.txtApematerno.setText(objPersona[2])
        self.ventana.txtNom1.setText(objPersona[3])
        self.ventana.txtNom2.setText(objPersona[4])
        self.ventana.txtDNI.setText(objPersona[5])
        self.ventana.txtDepartamento.setText(objPersona[6])
        self.ventana.txtProvincia.setText(objPersona[7])
        self.ventana.txtDistrito.setText(objPersona[8])
        self.ventana.txtDireccion.setText(objPersona[9])
        self.ventana.txtCelular.setText(str(objPersona[10]))
        self.ventana.txtCorreo.setText(objPersona[11])
        self.ventana.txtFecnacimiento.setText(str(objPersona[12]))
        if objPersona[13] == "M":
            self.ventana.rbMasculino.setChecked(True)
        else:
            self.ventana.rdFemenino.setChecked(True)

    def listarPersona(self):
        self.ventana.txtIdPersona.setEnabled(False)
        listaPersona = self.objPersonaRepository.listarPersona()
        cantidad = len(listaPersona)
        self.ventana.tblPersona.setRowCount(cantidad)
        fila = 0
        for persona in listaPersona:
            self.ventana.tblPersona.setItem(fila, 0, QTableWidgetItem(str(persona[0])))
            self.ventana.tblPersona.setItem(fila, 1, QTableWidgetItem(persona[1]))
            self.ventana.tblPersona.setItem(fila, 2, QTableWidgetItem(persona[2]))
            self.ventana.tblPersona.setItem(fila, 3, QTableWidgetItem(persona[3]))
            self.ventana.tblPersona.setItem(fila, 4, QTableWidgetItem(persona[4]))
            self.ventana.tblPersona.setItem(fila, 5, QTableWidgetItem(str(persona[5])))
            self.ventana.tblPersona.setItem(fila, 6, QTableWidgetItem(persona[6]))
            self.ventana.tblPersona.setItem(fila, 7, QTableWidgetItem(persona[7]))
            self.ventana.tblPersona.setItem(fila, 8, QTableWidgetItem(persona[8]))
            self.ventana.tblPersona.setItem(fila, 9, QTableWidgetItem(persona[9]))
            self.ventana.tblPersona.setItem(fila, 10, QTableWidgetItem(str(persona[10])))
            self.ventana.tblPersona.setItem(fila, 11, QTableWidgetItem(str(persona[11])))
            self.ventana.tblPersona.setItem(fila, 12, QTableWidgetItem(str(persona[12])))
            self.ventana.tblPersona.setItem(fila, 13, QTableWidgetItem(str(persona[13])))
            fila += 1
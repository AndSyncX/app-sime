from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.ModalidadRepository import ModalidadRepository
from model.Modalidad import Modalidad

class ModalidadController():
    
    def __init__(self) -> None:
        self.objModalidadRepository = ModalidadRepository()
        self.ventana = uic.loadUi("view/frmModalidad.ui")
        self.ventana.tblModalidad.cellClicked.connect(self.tblModalidadCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarModalidad()

    def limpiarDatos(self):
        self.ventana.txtIdModalidad.clear()
        self.ventana.txtDescripcion.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idmodalidad = self.ventana.txtIdModalidad.text()
        descripcion = self.ventana.txtDescripcion.text()
        newModalidad = Modalidad(idmodalidad, descripcion)
        if descripcion == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objModalidadRepository.insertarModalidad(newModalidad)
            self.listarModalidad()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Modalidad registrado exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        idmodalidad = self.ventana.txtIdModalidad.text()
        descripcion = self.ventana.txtDescripcion.text()
        newModalidad = Modalidad(idmodalidad, descripcion)
        if idmodalidad == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objModalidadRepository.actualizarModalidad(newModalidad)
            self.limpiarDatos()
            self.listarModalidad()
            QMessageBox.information(self.ventana, "Éxito", "Modalidad actualizada exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()
    
    def tblModalidadCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idmodalidad = self.ventana.tblModalidad.item(fila, 0).text()
        self.ventana.txtIdModalidad.setText(idmodalidad)
        objModalidad = self.objModalidadRepository.buscarModalidadID(idmodalidad)
        self.ventana.txtDescripcion.setText(str(objModalidad[1]))

    def listarModalidad(self):
        self.ventana.txtIdModalidad.setEnabled(False)
        listaModalidad = self.objModalidadRepository.listarModalidad()
        cantidad = len(listaModalidad)
        self.ventana.tblModalidad.setRowCount(cantidad)
        fila = 0
        for modalidad in listaModalidad:
            self.ventana.tblModalidad.setItem(fila, 0, QTableWidgetItem(str(modalidad[0])))
            self.ventana.tblModalidad.setItem(fila, 1, QTableWidgetItem(modalidad[1]))
            fila += 1
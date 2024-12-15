from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.DiaSemanaRepository import DiaSemanaRepository
from model.DiaSemana import DiaSemana

class DiaSemanaController():
    
    def __init__(self) -> None:
        self.objDiasemanaRepository = DiaSemanaRepository()
        self.ventana = uic.loadUi("view/frmDiaSemana.ui")
        self.ventana.tblDiasemana.cellClicked.connect(self.tblDiasemanaCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarDiasemana()

    def limpiarDatos(self):
        self.ventana.txtIdDiasemana.clear()
        self.ventana.txtDescripcion.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        iddiasemana = self.ventana.txtIdDiasemana.text()
        descripcion = self.ventana.txtDescripcion.text()
        newDiasemana = DiaSemana(iddiasemana, descripcion)
        if descripcion == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objDiasemanaRepository.insertarDiaSemana(newDiasemana)
            self.listarDiasemana()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Diasemana registrado exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        iddiasemana = self.ventana.txtIdDiasemana.text()
        descripcion = self.ventana.txtDescripcion.text()
        newDiasemana = DiaSemana(iddiasemana, descripcion)
        if iddiasemana == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objDiasemanaRepository.actualizarDiaSemana(newDiasemana)
            self.limpiarDatos()
            self.listarDiasemana()
            QMessageBox.information(self.ventana, "Éxito", "Diasemana actualizada exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()
    
    def tblDiasemanaCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        iddiasemana = self.ventana.tblDiasemana.item(fila, 0).text()
        self.ventana.txtIdDiasemana.setText(iddiasemana)
        objDiasemana = self.objDiasemanaRepository.buscarDiaSemanaID(iddiasemana)
        self.ventana.txtDescripcion.setText(objDiasemana[1])

    def listarDiasemana(self):
        self.ventana.txtIdDiasemana.setEnabled(False)
        listaDiasemana = self.objDiasemanaRepository.listarDiaSemana()
        cantidad = len(listaDiasemana)
        self.ventana.tblDiasemana.setRowCount(cantidad)
        fila = 0
        for diasemana in listaDiasemana:
            self.ventana.tblDiasemana.setItem(fila, 0, QTableWidgetItem(str(diasemana[0])))
            self.ventana.tblDiasemana.setItem(fila, 1, QTableWidgetItem(diasemana[1]))
            fila += 1
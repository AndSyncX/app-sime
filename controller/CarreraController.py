from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.CarreraRepository import CarreraRepository
from repository.ModalidadRepository import ModalidadRepository
from model.Carrera import Carrera

class CarreraController:
    
    def __init__(self) -> None:
        self.objCarreraRepository = CarreraRepository()
        self.objModalidadRepository = ModalidadRepository()
        self.ventana = uic.loadUi("view/frmCarrera.ui")
        self.ventana.tblCarrera.cellClicked.connect(self.tblCarreraCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarCarrera()
        self.listarModalidad()

    def limpiarDatos(self):
        self.ventana.txtIdCarrera.clear()
        self.ventana.txtNombre.clear()
        self.ventana.txtCreditos.clear()
        self.ventana.cboModalidad.setCurrentIndex(0)
        self.ventana.txtDuracion.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idcarrera = self.ventana.txtIdCarrera.text()
        nomcarrera = self.ventana.txtNombre.text()
        creditos = self.ventana.txtCreditos.text()
        cboModalidad = self.ventana.cboModalidad.currentData()
        duracion = self.ventana.txtDuracion.text()
        newCarrera = Carrera(idcarrera, nomcarrera, creditos, duracion, cboModalidad)
        if nomcarrera == "" or creditos == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objCarreraRepository.insertarCarrera(newCarrera)
            self.listarCarrera()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Carrera registrado exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        idcarrera = self.ventana.txtIdCarrera.text()
        nomcarrera = self.ventana.txtNombre.text()
        creditos = self.ventana.txtCreditos.text()
        cboModalidad = self.ventana.cboModalidad.currentData()
        duracion = self.ventana.txtDuracion.text()
        newCarrera = Carrera(idcarrera, nomcarrera, creditos, duracion, cboModalidad)
        if nomcarrera == "" or creditos == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objCarreraRepository.actualizarCarrera(newCarrera)
            self.limpiarDatos()
            self.listarCarrera()
            QMessageBox.information(self.ventana, "Éxito", "Carrera actualizada exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()
    
    def tblCarreraCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idcarrera = self.ventana.tblCarrera.item(fila, 0).text()
        self.ventana.txtIdCarrera.setText(idcarrera)
        objCarrera = self.objCarreraRepository.buscarCarreraID(idcarrera)
        self.ventana.txtNombre.setText(objCarrera[1])
        self.ventana.txtCreditos.setText(str(objCarrera[2]))
        self.ventana.cboModalidad.setCurrentText(objCarrera[4])
        self.ventana.txtDuracion.setText(str(objCarrera[3]))

    def listarCarrera(self):
        self.ventana.txtIdCarrera.setEnabled(False)
        listaCarrera = self.objCarreraRepository.listarCarrera()
        cantidad = len(listaCarrera)
        self.ventana.tblCarrera.setRowCount(cantidad)
        fila = 0
        for carrera in listaCarrera:
            self.ventana.tblCarrera.setItem(fila, 0, QTableWidgetItem(str(carrera[0])))
            self.ventana.tblCarrera.setItem(fila, 1, QTableWidgetItem(carrera[1]))
            self.ventana.tblCarrera.setItem(fila, 2, QTableWidgetItem(str(carrera[2])))
            self.ventana.tblCarrera.setItem(fila, 3, QTableWidgetItem(carrera[3]))
            self.ventana.tblCarrera.setItem(fila, 4, QTableWidgetItem(str(carrera[4])))
            fila += 1
    
    def listarModalidad(self):
        listaModalidad = self.objModalidadRepository.listarModalidad()
        for modalidad in listaModalidad:
            self.ventana.cboModalidad.addItem(
                modalidad[1],
                modalidad[0],
            )
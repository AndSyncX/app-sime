from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.CursoRepository import CursoRepository
from model.Curso import Curso

class CursoController():
    
    def __init__(self) -> None:
        self.objCursoRepository = CursoRepository()
        self.ventana = uic.loadUi("view/frmCurso.ui")
        self.ventana.tblCursos.cellClicked.connect(self.tblCursosCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarCurso()

    def limpiarDatos(self):
        self.ventana.txtIdcurso.clear()
        self.ventana.txtNombre.clear()
        self.ventana.txtCreditos.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idcurso = self.ventana.txtIdcurso.text()
        nomcurso = self.ventana.txtNombre.text()
        creditos = self.ventana.txtCreditos.text()
        newCurso = Curso(idcurso, nomcurso, creditos)
        if nomcurso == "" or creditos == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objCursoRepository.insertarCurso(newCurso)
            self.listarCurso()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Curso registrado exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        idcurso = self.ventana.txtIdcurso.text()
        nomcurso = self.ventana.txtNombre.text()
        creditos = self.ventana.txtCreditos.text()
        newCurso = Curso(idcurso, nomcurso, creditos)
        if idcurso == "" or nomcurso == "" or creditos == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objCursoRepository.actualizarCurso(newCurso)
            self.limpiarDatos()
            self.listarCurso()
            QMessageBox.information(self.ventana, "Éxito", "Curso actualizado exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()
    
    def tblCursosCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idcurso = self.ventana.tblCursos.item(fila, 0).text()
        self.ventana.txtIdcurso.setText(idcurso)
        objCurso = self.objCursoRepository.buscarCursoID(idcurso)
        self.ventana.txtNombre.setText(objCurso[1])
        self.ventana.txtCreditos.setText(str(objCurso[2]))

    def listarCurso(self):
        self.ventana.txtIdcurso.setEnabled(False)
        listarCurso = self.objCursoRepository.listarCurso()
        cantidad = len(listarCurso)
        self.ventana.tblCursos.setRowCount(cantidad)
        fila = 0
        for curso in listarCurso:
            self.ventana.tblCursos.setItem(fila, 0, QTableWidgetItem(str(curso[0])))
            self.ventana.tblCursos.setItem(fila, 1, QTableWidgetItem(curso[1]))
            self.ventana.tblCursos.setItem(fila, 2, QTableWidgetItem(str(curso[2])))
            fila += 1
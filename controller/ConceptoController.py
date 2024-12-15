from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.ConceptoRepository import ConceptoRepository
from model.Concepto import Concepto

class ConceptoController():
    
    def __init__(self) -> None:
        self.objConceptoRepository = ConceptoRepository()
        self.ventana = uic.loadUi("view/frmConcepto.ui")
        self.ventana.tblConcepto.cellClicked.connect(self.tblConceptoCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarConcepto()

    def limpiarDatos(self):
        self.ventana.txtIdconcepto.clear()
        self.ventana.txtDescripcion.clear()
        self.ventana.txtMonto.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idconcepto = self.ventana.txtIdconcepto.text()
        descripcion = self.ventana.txtDescripcion.text()
        monto = self.ventana.txtMonto.text()
        newConcepto = Concepto(idconcepto, descripcion, monto)
        if descripcion == "" or monto == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objConceptoRepository.insertarConcepto(newConcepto)
            self.listarConcepto()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Concepto registrado exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        idconcepto = self.ventana.txtIdconcepto.text()
        descripcion = self.ventana.txtDescripcion.text()
        monto = self.ventana.txtMonto.text()
        newConcepto = Concepto(idconcepto, descripcion, monto)
        if idconcepto == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objConceptoRepository.actualizarConcepto(newConcepto)
            self.limpiarDatos()
            self.listarConcepto()
            QMessageBox.information(self.ventana, "Éxito", "Concepto actualizada exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()
    
    def tblConceptoCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idconcepto = self.ventana.tblConcepto.item(fila, 0).text()
        self.ventana.txtIdconcepto.setText(idconcepto)
        objConcepto = self.objConceptoRepository.buscarConceptoID(idconcepto)
        self.ventana.txtDescripcion.setText(str(objConcepto[1]))
        self.ventana.txtMonto.setText(str(objConcepto[2]))

    def listarConcepto(self):
        self.ventana.txtIdconcepto.setEnabled(False)
        listaConcepto = self.objConceptoRepository.listarConcepto()
        cantidad = len(listaConcepto)
        self.ventana.tblConcepto.setRowCount(cantidad)
        fila = 0
        for concepto in listaConcepto:
            self.ventana.tblConcepto.setItem(fila, 0, QTableWidgetItem(str(concepto[0])))
            self.ventana.tblConcepto.setItem(fila, 1, QTableWidgetItem(str(concepto[1])))
            self.ventana.tblConcepto.setItem(fila, 2, QTableWidgetItem(str(concepto[2])))
            fila += 1
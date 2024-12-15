from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.DetalleRepository import DetalleRepository
from repository.CuotaRepository import CuotaRepository
from repository.ConceptoRepository import ConceptoRepository
from model.Detalle import Detalle

class DetalleController():
    
    def __init__(self) -> None:
        self.objDetalleRepository = DetalleRepository()
        self.objConceptoRepository = ConceptoRepository()
        self.objCuotaRepository = CuotaRepository()
        self.ventana = uic.loadUi("view/frmDetalle.ui")
        self.ventana.tblDetalle.cellClicked.connect(self.tblDetalleCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarDetalle()
        self.listarConcepto()
        #self.listarCuota()

    def limpiarDatos(self):
        self.ventana.txtIdDetalle.clear()
        self.ventana.cboCuota.setCurrentIndex(0)
        self.ventana.cboConcepto.setCurrentIndex(0)
        self.ventana.txtFeDetalle.clear()
        self.ventana.txtMonto.clear()
        self.ventana.txtObservacion.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        iddetalle = self.ventana.txtIdDetalle.text()
        cuota = self.ventana.cboCuota.currentData()
        concepto = self.ventana.cboConcepto.currentData()
        fe_detalle = self.ventana.txtFeDetalle.text()
        monto = self.ventana.txtMonto.text()
        observaciones = self.ventana.txtObservacion.text()

        newDetalle = Detalle(iddetalle, cuota, concepto, fe_detalle, monto, observaciones)
        if fe_detalle == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objDetalleRepository.insertarDetalle(newDetalle)
            self.listarDetalle()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Detalle registrado exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        iddetalle = self.ventana.txtIdDetalle.text()
        estudiante = self.ventana.cboEstudiante.currentData()
        detalle = self.ventana.cboConcepto.currentData()
        matricula = self.ventana.cboMatricula.currentData()
        fe_pago = self.ventana.txtFePago.text()
        monto = self.ventana.txtMonto.text()
        estado = self.ventana.txtEstado.text()

        newDetalle = Detalle(iddetalle, estudiante, detalle, matricula, fe_pago, monto, estado)
        if iddetalle == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objDetalleRepository.actualizarDetalle(newDetalle)
            self.limpiarDatos()
            self.listarDetalle()
            QMessageBox.information(self.ventana, "Éxito", "Detalle actualizado exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()
    
    def tblDetalleCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        iddetalle = self.ventana.tblDetalle.item(fila, 0).text()
        self.ventana.txtIdDetalle.setText(iddetalle)
        objDetalle = self.objDetalleRepository.buscarDetalleID(iddetalle)
        self.ventana.cboCuota.setCurrentText(str(objDetalle[1]))
        self.ventana.cboConcepto.setCurrentText(str(objDetalle[2]))
        self.ventana.txtFeDetalle.setText(str(objDetalle[3]))
        self.ventana.txtMonto.setText(str(objDetalle[4]))
        self.ventana.txtObservacion.setText(str(objDetalle[5]))

    def listarDetalle(self):
        self.ventana.txtIdDetalle.setEnabled(False)
        listaDetalle = self.objDetalleRepository.listarDetalle()
        cantidad = len(listaDetalle)
        self.ventana.tblDetalle.setRowCount(cantidad)
        fila = 0
        for detalle in listaDetalle:
            self.ventana.tblDetalle.setItem(fila, 0, QTableWidgetItem(str(detalle[0])))
            self.ventana.tblDetalle.setItem(fila, 1, QTableWidgetItem(str(detalle[1])))
            self.ventana.tblDetalle.setItem(fila, 2, QTableWidgetItem(str(detalle[2])))
            self.ventana.tblDetalle.setItem(fila, 3, QTableWidgetItem(str(detalle[3])))
            self.ventana.tblDetalle.setItem(fila, 4, QTableWidgetItem(str(detalle[4])))
            self.ventana.tblDetalle.setItem(fila, 5, QTableWidgetItem(str(detalle[5])))
            fila += 1

    def listarEstudiante(self):
        listaEstudiante = self.objEstudianteRepository.listarEstudiantePersona()
        for estudiante in listaEstudiante:
            self.ventana.cboEstudiante.addItem(
                estudiante[1],
                estudiante[0]
            )
    
    def listarConcepto(self):
        listaConcepto = self.objConceptoRepository.listarConcepto()
        for concepto in listaConcepto:
            self.ventana.cboConcepto.addItem(
                concepto[1],
                concepto[0]
            )

    def listarMatricula(self):
        listaMatricula = self.objMatriculaRepository.listarMatricula()
        for matricula in listaMatricula:
            self.ventana.cboMatricula.addItem(
                str(matricula[0]),
                matricula[0]
            )
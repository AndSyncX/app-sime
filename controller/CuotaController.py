from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.CuotaRepository import CuotaRepository
from repository.EstudianteRepository import EstudianteRepository
from repository.ConceptoRepository import ConceptoRepository
from repository.MatriculaRepository import MatriculaRepository
from model.Cuota import Cuota


class CuotaController():
    
    def __init__(self) -> None:
        self.objCuotaRepository = CuotaRepository()
        self.objEstudianteRepository = EstudianteRepository()
        self.objConceptoRepository = ConceptoRepository()
        self.objMatriculaRepository = MatriculaRepository()
        self.ventana = uic.loadUi("view/frmCuota.ui")
        self.ventana.tblCuota.cellClicked.connect(self.tblCuotaCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarCuota()
        self.listarEstudiante()
        self.listarMatricula()
        self.listarConcepto()

    def limpiarDatos(self):
        self.ventana.txtIdCuota.clear()
        self.ventana.cboEstudiante.setCurrentIndex(0)
        self.ventana.cboConcepto.setCurrentIndex(0)
        self.ventana.cboMatricula.setCurrentIndex(0)
        self.ventana.txtFePago.clear()
        self.ventana.txtMonto.clear()
        self.ventana.txtEstado.clear()
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idcuota = self.ventana.txtIdCuota.text()
        estudiante = self.ventana.cboEstudiante.currentData()
        cuota = self.ventana.cboConcepto.currentData()
        matricula = self.ventana.cboMatricula.currentData()
        fe_pago = self.ventana.txtFePago.text()
        monto = self.ventana.txtMonto.text()
        estado = self.ventana.txtEstado.text()

        newCuota = Cuota(idcuota, estudiante, cuota, matricula, fe_pago, monto, estado)
        if estado == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objCuotaRepository.insertarCuota(newCuota)
            self.listarCuota()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Cuota registrado exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        idcuota = self.ventana.txtIdCuota.text()
        estudiante = self.ventana.cboEstudiante.currentData()
        cuota = self.ventana.cboConcepto.currentData()
        matricula = self.ventana.cboMatricula.currentData()
        fe_pago = self.ventana.txtFePago.text()
        monto = self.ventana.txtMonto.text()
        estado = self.ventana.txtEstado.text()

        newCuota = Cuota(idcuota, estudiante, cuota, matricula, fe_pago, monto, estado)
        if idcuota == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objCuotaRepository.actualizarCuota(newCuota)
            self.limpiarDatos()
            self.listarCuota()
            QMessageBox.information(self.ventana, "Éxito", "Cuota actualizado exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()
    
    def tblCuotaCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idcuota = self.ventana.tblCuota.item(fila, 0).text()
        self.ventana.txtIdCuota.setText(idcuota)
        objCuota = self.objCuotaRepository.buscarCuotaID(idcuota)
        self.ventana.cboEstudiante.setCurrentText(str(objCuota[1]))
        self.ventana.cboConcepto.setCurrentText(str(objCuota[2]))
        self.ventana.cboMatricula.setCurrentText(str(objCuota[3]))
        self.ventana.txtFePago.setText(str(objCuota[4]))
        self.ventana.txtMonto.setText(str(objCuota[5]))
        self.ventana.txtEstado.setText(str(objCuota[6]))

    def listarCuota(self):
        self.ventana.txtIdCuota.setEnabled(False)
        listaCuota = self.objCuotaRepository.listarCuota()
        cantidad = len(listaCuota)
        self.ventana.tblCuota.setRowCount(cantidad)
        fila = 0
        for cuota in listaCuota:
            self.ventana.tblCuota.setItem(fila, 0, QTableWidgetItem(str(cuota[0])))
            self.ventana.tblCuota.setItem(fila, 1, QTableWidgetItem(str(cuota[1])))
            self.ventana.tblCuota.setItem(fila, 2, QTableWidgetItem(str(cuota[2])))
            self.ventana.tblCuota.setItem(fila, 3, QTableWidgetItem(str(cuota[3])))
            self.ventana.tblCuota.setItem(fila, 4, QTableWidgetItem(str(cuota[4])))
            self.ventana.tblCuota.setItem(fila, 5, QTableWidgetItem(str(cuota[5])))
            self.ventana.tblCuota.setItem(fila, 6, QTableWidgetItem(str(cuota[6])))
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
    
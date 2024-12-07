from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.SeccionRepository import SeccionRepository
from repository.CursoRepository import CursoRepository
from repository.HorarioRepository import HorarioRepository
from repository.DocenteRepository import DocenteRepository
from model.Seccion import Seccion

class SeccionController():
    
    def __init__(self) -> None:
        self.objSeccionRepository = SeccionRepository()
        self.objCursoRepository = CursoRepository()
        self.objHorarioRepository = HorarioRepository()
        self.objDocenteRepository = DocenteRepository()
        self.ventana = uic.loadUi("view/frmSeccion.ui")
        self.ventana.tblSeccion.cellClicked.connect(self.tblSeccionCellClick)
        """self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)"""
        self.listarCurso()
        self.listarSeccion()
        self.listarHorario()
        self.listarDocente()
    
    """def limpiarDatos(self):
        self.ventana.txtIdhorario.clear()
        self.ventana.txtHorainicio.clear()
        self.ventana.txtHorafin.clear()
        self.ventana.cboDiasemana.setCurrentIndex(0)
        self.ventana.btnRegistrar.setEnabled(True)

    def btnRegistrarClick(self):
        idHorario = self.ventana.txtIdhorario.text()
        horaInicio = self.ventana.txtHorainicio.text()
        HoraFin = self.ventana.txtHorafin.text()
        diaSemana = self.ventana.cboDiasemana.currentData()
        newHorario = Horario(idHorario, horaInicio, HoraFin, diaSemana)
        if horaInicio == "" or HoraFin == "":
            QMessageBox.information(self.ventana, "Error", "Campos incompletos", QMessageBox.Ok)
        else:
            self.objHorarioRepository.insertarHorario(newHorario)
            self.listarHorario()
            self.limpiarDatos()
            QMessageBox.information(self.ventana, "Éxito", "Carrera registrado exitosamente", QMessageBox.Ok)

    def btnActualizarClick(self):
        idHorario = self.ventana.txtIdhorario.text()
        horaInicio = self.ventana.txtHorainicio.text()
        HoraFin = self.ventana.txtHorafin.text()
        diaSemana = self.ventana.cboDiasemana.currentData()
        newHorario = Horario(idHorario, horaInicio, HoraFin, diaSemana)
        if idHorario == "" or horaInicio == "" or HoraFin == "":
            QMessageBox.information(self.ventana, "Error", "No hay datos seleccionados", QMessageBox.Ok)
        else:
            self.objHorarioRepository.actualizarHorario(newHorario)
            self.limpiarDatos()
            self.listarHorario()
            QMessageBox.information(self.ventana, "Éxito", "Carrera actualizada exitosamente", QMessageBox.Ok)
            self.ventana.btnRegistrar.setEnabled(True)

    def btnLimpiarClick(self):
        self.limpiarDatos()"""
    
    def tblSeccionCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idseccion = self.ventana.tblSeccion.item(fila, 0).text()
        self.ventana.txtIdseccion.setText(idseccion)
        objSeccion = self.objSeccionRepository.buscarSeccionID(idseccion)
        self.ventana.cboDocente.setCurrentText(objSeccion[1])
        self.ventana.cboHorario.setCurrentText(str(objSeccion[2]))
        self.ventana.cboCurso.setCurrentText(objSeccion[3])
        self.ventana.txtNombre.setText(objSeccion[4])
        self.ventana.txtCapacidad.setText(str(objSeccion[5]))

    def listarSeccion(self):
        self.ventana.txtIdseccion.setEnabled(False)
        listaSeccion = self.objSeccionRepository.listarSeccion()
        cantidad = len(listaSeccion)
        self.ventana.tblSeccion.setRowCount(cantidad)
        fila = 0
        for seccion in listaSeccion:
            self.ventana.tblSeccion.setItem(fila, 0, QTableWidgetItem(str(seccion[0])))
            self.ventana.tblSeccion.setItem(fila, 1, QTableWidgetItem(str(seccion[1])))
            self.ventana.tblSeccion.setItem(fila, 2, QTableWidgetItem(str(seccion[2])))
            self.ventana.tblSeccion.setItem(fila, 3, QTableWidgetItem(str(seccion[3])))
            self.ventana.tblSeccion.setItem(fila, 4, QTableWidgetItem(str(seccion[4])))
            self.ventana.tblSeccion.setItem(fila, 5, QTableWidgetItem(str(seccion[5])))
            fila += 1
    
    def listarCurso(self):
        listaCurso = self.objCursoRepository.listarCurso()
        for curso in listaCurso:
            self.ventana.cboCurso.addItem(
                curso[1],
                curso[0]
            )
    
    def listarHorario(self):
        listaHorario = self.objHorarioRepository.listarHorario()
        for horario in listaHorario:
            self.ventana.cboHorario.addItem(
                str(horario[1]),
                horario[0]
            )
    
    def listarDocente(self):
        listaDocente = self.objDocenteRepository.listarDocente()
        for docente in listaDocente:
            self.ventana.cboDocente.addItem(
                docente[1] + ", " + docente[3],
                docente[0]
            )
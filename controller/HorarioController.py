from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from repository.HorarioRepository import HorarioRepository
from repository.DiaSemanaRepository import DiaSemanaRepository
from model.Horario import Horario

class HorarioController():
    
    def __init__(self) -> None:
        self.objHorarioRepository = HorarioRepository()
        self.objDiaSemanaRepository = DiaSemanaRepository()
        self.ventana = uic.loadUi("view/frmHorario.ui")
        self.ventana.tblHorarios.cellClicked.connect(self.tblHorarioCellClick)
        self.ventana.btnRegistrar.clicked.connect(self.btnRegistrarClick)
        self.ventana.btnActualizar.clicked.connect(self.btnActualizarClick)
        self.ventana.btnLimpiar.clicked.connect(self.btnLimpiarClick)
        self.listarHorario()
        self.listarDiaSemana()
    
    def limpiarDatos(self):
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
        self.limpiarDatos()
    
    def tblHorarioCellClick(self, fila):
        self.ventana.btnRegistrar.setEnabled(False)
        idhorario = self.ventana.tblHorarios.item(fila, 0).text()
        self.ventana.txtIdhorario.setText(idhorario)
        objHorario = self.objHorarioRepository.buscarHorarioID(idhorario)
        self.ventana.txtHorainicio.setText(str(objHorario[1]))
        self.ventana.txtHorafin.setText(str(objHorario[2]))
        self.ventana.cboDiasemana.setCurrentText(objHorario[3])

    def listarHorario(self):
        self.ventana.txtIdhorario.setEnabled(False)
        listaHorario = self.objHorarioRepository.listarHorario()
        cantidad = len(listaHorario)
        self.ventana.tblHorarios.setRowCount(cantidad)
        fila = 0
        for horario in listaHorario:
            self.ventana.tblHorarios.setItem(fila, 0, QTableWidgetItem(str(horario[0])))
            self.ventana.tblHorarios.setItem(fila, 1, QTableWidgetItem(str(horario[1])))
            self.ventana.tblHorarios.setItem(fila, 2, QTableWidgetItem(str(horario[2])))
            self.ventana.tblHorarios.setItem(fila, 3, QTableWidgetItem(str(horario[3])))
            fila += 1
    
    def listarDiaSemana(self):
        listaDiaSemana = self.objDiaSemanaRepository.listarDiaSemana()
        for dia in listaDiaSemana:
            self.ventana.cboDiasemana.addItem(
                dia[1],
                dia[0]
            )
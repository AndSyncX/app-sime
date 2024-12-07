class Cuota:
    
    def __init__(self, _id_cuota, _id_estudiante, _id_concepto, _id_matricula, _fec_pago, _monto, _estado):
        self.id_cuota = _id_cuota
        self.id_estudiante = _id_estudiante
        self.id_concepto = _id_concepto
        self.id_matricula = _id_matricula
        self.fec_pago = _fec_pago
        self.monto = _monto
        self.estado = _estado
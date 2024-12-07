from model.Persona import Persona

class Docente(Persona):
    
    def __init__(self, _id_persona, _ape_paterno, _ape_materno, _nom1, _nom2, _dni, _departamento, _provincia, 
                 _distrito, _direccion, _celular, _correo, _fec_nacimiento, _estado_civil, _sexo, _id_docente, 
                 _especialidad):
        super().__init__(_id_persona, _ape_paterno, _ape_materno, _nom1, _nom2, _dni, _departamento, _provincia, 
                         _distrito, _direccion, _celular, _correo, _fec_nacimiento, _estado_civil, _sexo)
        self.id_docente = _id_docente
        self.especialidad = _especialidad
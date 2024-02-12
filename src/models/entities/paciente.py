class Paciente():

    def __init__(self, id_paciente, nombre=None, telefono=None, email=None, imagen_uri=None, id_medico=None) -> None:
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.imagen_uri = imagen_uri
        self.id_medico = id_medico

    def to_JSON(self):
        return {
            'id_paciente': self.id_paciente,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'email': self.email,
            'imagen_uri': self.imagen_uri,
            'id_medico': self.id_medico
        }
        



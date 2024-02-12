from database.db import get_connection
from .entities.paciente import Paciente

class PacienteModel():

    @classmethod
    def get_pacientes(self):
        try:
            connection=get_connection()
            pacientes=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_paciente, nombre, telefono, email, imagen_uri, id_medico FROM pacientes order by id_paciente ASC")
                resultset=cursor.fetchall()

                for row in resultset:
                    paciente=Paciente(row[0], row[1], row[2], row[3], row[4], row[5])
                    pacientes.append(paciente.to_JSON())

            connection.close()
            return pacientes
        
        except Exception as ex:
            raise Exception(ex)

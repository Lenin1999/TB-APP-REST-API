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


class PacienteModelInsert():
    @classmethod
    def post_pacientes(cls, id_medico, nombre, telefono, email, imagen_uri):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO pacientes (id_medico, nombre, telefono, email, imagen_uri) VALUES (%s, %s, %s, %s, %s)",
                               (id_medico, nombre, telefono, email, imagen_uri))
            connection.commit()  # Es importante hacer commit después de una operación de escritura en la base de datos

            # Puedes retornar algo si lo necesitas, por ejemplo, el ID del paciente insertado
            # En este caso, el ID es un valor serial, por lo que puedes obtenerlo después del INSERT
            # Ejemplo: paciente_id = cursor.lastrowid

            connection.close()
            return "Paciente insertado exitosamente"
        
        except Exception as ex:
            raise Exception(ex)
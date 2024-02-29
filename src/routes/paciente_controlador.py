from flask import Blueprint, jsonify
from flask import Flask, request, jsonify

#modelos
from models.paciente_modelo import PacienteModel
from models.paciente_modelo import PacienteModelInsert

main=Blueprint('paciente_blueprint', __name__)

@main.route('/')
def get_pacientes():
    try:
        pacientes = PacienteModel.get_pacientes()
        return jsonify(pacientes)
    except Exception as ex:
        return jsonify({'messaage': str(ex)}), 500
    


@main.route('/crear_paciente', methods=['POST'])
def crear_paciente():
    try:
        # Obtener los datos del paciente del cuerpo de la solicitud
        id_medico = request.form.get('id_medico')
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        imagen_uri = request.form.get('imagen_uri')

        print(id_medico);
        print(nombre);
        print(telefono);
        print(email);
        

        # Insertar el paciente en la base de datos
        resultado = PacienteModelInsert.post_pacientes(id_medico, nombre, telefono, email, imagen_uri)
        print(resultado);
        # Retornar una respuesta
        return jsonify({"mensaje": resultado}), 201  # 201 significa "Created"
    
    except Exception as ex:
        # Manejar errores
        return jsonify({"error": str(ex)}), 500
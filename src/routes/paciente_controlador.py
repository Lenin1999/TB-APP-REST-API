from flask import Blueprint, jsonify

#modelos
from models.paciente_modelo import PacienteModel

main=Blueprint('paciente_blueprint', __name__)

@main.route('/')
def get_pacientes():
    try:
        pacientes = PacienteModel.get_pacientes()
        return jsonify(pacientes)
    except Exception as ex:
        return jsonify({'messaage': str(ex)}), 500
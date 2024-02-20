from flask import Flask
from config import config
from flask_cors import CORS

#Rutas
from routes import paciente_controlador

app = Flask(__name__)

CORS(app) 

app.register_blueprint(paciente_controlador.main, url_prefix='/api/pacientes')


def page_not_found(error):
    return "<h1>Not found page</h1>", 404

app.config.from_object(config['development'])

if __name__ == '__main__':
    
    app.run(host='192.168.1.8', port=5000)

    #Blueprints
    app.register_error_handler(404, page_not_found)

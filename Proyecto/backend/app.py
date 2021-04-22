# CREAR TODA LAS CLASES Y LOGICA DEL JUEGO EN LA CARPETA game

# librerias y framework
from flask import Flask;
from flask_restful import Resource, Api

# importaciones del proyecto
from services.storageService import storageService
from game.testClass import testClass

app = Flask(__name__)
api = Api(app)


class createGame(Resource):
    def get(self):
        # 
        # aca testear los metodos y las clases creadas
        # 
        return {'status': 'OK'}

api.add_resource(createGame, '/test')

if __name__ == '__main__':
    app.run(debug=True);

# python -m venv myvenv crear entorno virtual
# myvenv\Scripts\activate comando para iniciar entorno virtual
# set “FLASK_ENV=development” poner el entorno virutal en modo de desarrollo
# set FLASK_APP=main.py setear main.py como nuestra aplicacion de flask
# set FLASK_DEBUG=1 mostrar el debug en el html
# flask run comando para iniciar el servidor

# pip freeze >> requirements.txt guardar depedencias en el txt
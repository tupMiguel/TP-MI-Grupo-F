import json
class JugadorModel:
    def __init__(self, idPlayer, nombre):
        self.idPlayer =  idPlayer;
        self.nombre = nombre;
    def __repr__(self):
        return json.dumps(self.__dict__) 
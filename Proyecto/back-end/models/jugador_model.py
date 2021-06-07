import json


class JugadorModel:
    def __init__(self, idPlayer, nombre: str, dados_ataque=5, dados_defensa=5):
        self.idPlayer = idPlayer
        self.nombre = nombre
        self.dados_ataque = dados_ataque
        self.dados_defensa = dados_defensa

    def __repr__(self):
        return json.dumps(self.__dict__)

    def esPosibleAtacar(self):
        if self.dados_ataque >= 1:
            return True

    def actualizarDados(self):
        self.dados_ataque = 5
        self.dados_defensa = 5
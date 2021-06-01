from .pais_model import PaisModel
from .jugador_model import JugadorModel
import json

class PartidaModel:
    def __init__(self, idJuego: str, salaLlena: bool, jugadores: list[JugadorModel], tablero: list[list[PaisModel]], cantPaises: int):
        self.idJuego = idJuego
        self.salaLlena = salaLlena
        self.jugadores = jugadores
        self.tablero = tablero
        self.cantPaises = cantPaises
    
    def __repr__(self):
        return json.dumps(self.__dict__)
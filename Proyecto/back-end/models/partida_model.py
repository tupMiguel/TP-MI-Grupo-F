import json

from .pais_model import PaisModel
from .jugador_model import JugadorModel


class PartidaModel:
    def __init__(self, idJuego: str, salaLlena: bool, jugadores: list[JugadorModel], tablero: list[list[PaisModel]], cantPaises: int):
        self.idJuego = idJuego
        self.salaLlena = salaLlena
        self.jugadores = jugadores
        self.tablero = tablero
        self.cantPaises = cantPaises
        self.partida_en_proceso = True
        self.idProximoJugadorEsperado = 1

    def __repr__(self):
        return json.dumps(self.__dict__)

    def terminarTurno(self):

        if self.idProximoJugadorEsperado >= 4:
            self.idProximoJugadorEsperado = 1
            return

        self.idProximoJugadorEsperado += 1

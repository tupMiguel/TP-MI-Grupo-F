from models.partida_model import PartidaModel
from dataclasses import dataclass
from services.baseDeDatos_service import BaseDeDatosService


@dataclass
class PartidaController:

    baseDeDatos = BaseDeDatosService();


    def ataque(self, idJugadorAtancante: str ,coordX: int, coordY: int, partida: PartidaModel):

        if (partida.tablero[coordX][coordY].duenioId != idJugadorAtancante):
            partida.tablero[coordX][coordY].duenioId = idJugadorAtancante

        self.baseDeDatos.add_data(str(partida.__dict__));
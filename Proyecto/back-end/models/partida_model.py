from dataclasses import dataclass

from .pais_model import PaisModel
from .jugador_model import JugadorModel

@dataclass
class PartidaModel:
    idJuego: str;
    salaLlena: bool;
    jugadores: list[JugadorModel];
    tablero: list[list[PaisModel]];
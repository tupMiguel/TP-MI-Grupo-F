from models.partida_model import PartidaModel
from models import pais_model 
from dataclasses import dataclass
from services.baseDeDatos_service import BaseDeDatosService
from globals import PAISES
import random

@dataclass
class PartidaController:

    baseDeDatos = BaseDeDatosService();


    def ataque(self, idJugadorAtancante: str ,coordX: int, coordY: int, partida: PartidaModel):

        if (partida.tablero[coordX][coordY].duenioId != idJugadorAtancante):
            partida.tablero[coordX][coordY].duenioId = idJugadorAtancante

        self.baseDeDatos.add_data(str(partida.__dict__));

    def colocarPaises(self, matriz):
        """
        matriz: array bidimensional, llena de 0 y 1
        return: array bidimensional, reemplazando cada 1 por un objeto PaisModel
        """
        contador = 0
        for fila in matriz:
            for columna in matriz:
                if matriz[fila][columna] == 1:
                    matriz[fila][columna] = pais_model.PaisModel(PAISES[contador],"","")
                    contador += 1 
        return matriz
    
    def mezclarPaises(self, lista_Paises):
        """
        lista_Paises: lista[str], array de strings conteniendo nombres de paises
        return: None
        """
        random.shuffle(lista_Paises)
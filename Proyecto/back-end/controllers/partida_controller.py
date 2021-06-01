from models.partida_model import PartidaModel
from models import pais_model 
from dataclasses import dataclass
from services.baseDeDatos_service import BaseDeDatosService
from .globals import PAISES
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
        Introduce objetos PaisModel dentro de una matriz

        matriz: array bidimensional, contendra enteros 0 y 1
        return: array bidimensional, reemplaza cada entero 1 por un objeto PaisModel con un nombre en su propiedad
        """
        contador = 0
        for idxf, fila in enumerate(matriz):
            for idxc, columna in enumerate(matriz):
                if matriz[idxf][idxc] == 1:
                    matriz[idxf][idxc] = pais_model.PaisModel(PAISES[contador],"","")
                    contador += 1 
        return matriz
    
    def mezclarPaises(self, lista_Paises):
        """
        Desordena los elementos de manera aleatoria de un array

        lista_Paises: list[str], array de strings conteniendo nombres de paises
        return: None
        """
        random.shuffle(lista_Paises)
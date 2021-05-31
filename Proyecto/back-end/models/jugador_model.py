from pais_model import Pais 
class Jugador():
       
            
    def __init__(self, nombre, idplayer):
        self.nombre = nombre 
        self.idplayer = idplayer
        self.dadosAtaque=5  #chances para atacar
        self.dadosDefensa=5 #chances para defenderse
        self.lista_paises = []  #Lista que guarda los paises asignados y los paises limitrofes a quienes puede atacar
    def add_pais(self, paises):
        self.lista_paises.append(paises)






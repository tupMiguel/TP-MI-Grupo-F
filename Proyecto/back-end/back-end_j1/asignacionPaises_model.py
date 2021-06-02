#funcion que define la asignacion de los paises a cada jugador
import random
from paisesDisponibles_model import *
#from jugador_model import Jugador
#from pais_model import Pais


class asignacionDePaises():
    # funcion que recibe una matriz de 0 y 1, los '1' los reemplaza por paises elegidos al azar, tambien guarda la posicion.
    # nunca se repiten los paises aunque la matriz sea la misma
    def crearMatrizPais(matriz):
        for fila in range(len(matriz)):
            for columna in range(len(matriz[0])):
                if matriz[fila][columna] == 1:
                    nuevoPais = [random.choice(PAISES),fila,columna]
                    matriz[fila][columna] = nuevoPais
                    
                else:
                    nuevoPais = "Agua"
                    matriz[fila][columna] = nuevoPais

        return matriz   



    #matriz a modo de ejemplo
    matrizDePrueba = [
    [0,1,1,1,0,1],
    [1,0,1,1,1,1],
    [1,1,1,1,0,0]
     ]  
    
    
    matrizConPaises = [[]]
    #llamada al metodo solo para ver el funcionamiento
    matrizConPaises = crearMatrizPais(matrizDePrueba)
    print (matrizConPaises)

    
    #separo los paises de la matriz
    def ObtenerListaPaises(matriz):
        listaPaisesOrdenada = []
        
        for fila in range(len(matriz)):
            for columna in range(len(matriz[0])):
                if matriz[fila][columna] != 'Agua':
                    listaPaisesOrdenada.append(matriz[fila][columna])
                    
        
        return(listaPaisesOrdenada)    
    
    #llamada al metodo solo para ver el funcionamiento
    listaDesordenada = asignarPaisesAJugadores(matrizConPaises)
    #los paises se tienen que asignar de acuerdo a la cantidad de jugadores
    print(listaDesordenada)
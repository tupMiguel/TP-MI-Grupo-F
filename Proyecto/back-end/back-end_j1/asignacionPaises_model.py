#funcion que define la asignacion de los paises a cada jugador
import random
from paisesDisponibles_model import *
from random import shuffle
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
    print("Matriz con paises y Agua: ")
    print(" ")
    print (matrizConPaises)

    
    #separo los paises de la matriz
    def ObtenerListaPaises(matriz):
        listaPaises = []
        for fila in range(len(matriz)):
            for columna in range(len(matriz[0])):
                if matriz[fila][columna] != 'Agua':
                    listaPaises.append(matriz[fila][columna])
                    
        
        return(listaPaises)    
    
    #llamada al metodo solo para ver el funcionamiento
    listaPaisesAleatorios = ObtenerListaPaises(matrizConPaises)
    #los paises se tienen que asignar de acuerdo a la cantidad de jugadores
    print(" ")
    print(" Lista de solo paises ")
    print(" ")
    print(listaPaisesAleatorios)
    #desordeno la lista para que la eleccion sea al azar
    shuffle(listaPaisesAleatorios)
    print(" ")
    print(" Lista de paises mezclados para asignarlos al azar ")
    print(" ")
    print(listaPaisesAleatorios)

    #funciones para dividir la lista de acuerdo a la cantidad de jugadores

    def dividirListaEn2(lista_paises):
        mitad = len(lista_paises)//2
        return (lista_paises[:mitad], lista_paises[mitad:])
    
    def asignarPaises(cantJugadores):
        if cantJugadores == 2:
            listaPaisesJugador1, listaPaisesJugador2 = dividirListaEn2(listaPaisesAleatorios)
        return (listaPaisesJugador1, listaPaisesJugador2)           
         
    listaPaisesJugador1, listaPaisesJugador2 = asignarPaises(2)

    print("lista paises jugador 1:")
    print(listaPaisesJugador1)
    print("lista paises jugador 2:")
    print(listaPaisesJugador2)
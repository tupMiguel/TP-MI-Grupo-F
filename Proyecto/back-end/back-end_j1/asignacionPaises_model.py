#funciones que definen la asignacion de los paises a cada jugador
#los print solo se colocan solo a modo de ejemplo para ver la salida de las funciones

import random
from paisesDisponibles_model import *
from random import shuffle



#class asignacionDePaises():
    # funcion que recibe una matriz de 0 y 1, los '1' los reemplaza por paises elegidos al azar, tambien guarda la posicion.
    # nunca se repiten los paises aunque la matriz sea la misma
def crearMatrizPais(matriz):
    paisesParaElegir = random.sample(PAISES, 50)
    print("PAISES PARA ELEGIR:")
    print(paisesParaElegir)
    cont = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == 1:
                nuevoPais = [paisesParaElegir[cont],fila,columna]
                matriz[fila][columna] = nuevoPais
                cont = cont + 1    
            else:
                nuevoPais = "Agua"
                matriz[fila][columna] = nuevoPais

    return matriz   



    #matriz a modo de ejemplo
matrizDePrueba = [
    [0,1,1,1,0,1],
    [1,0,1,1,1,1],
    [1,1,0,1,0,0]
     ]  
    
    
matrizConPaises = [[]]
    #llamada al metodo solo para ver el funcionamiento
matrizConPaises = crearMatrizPais(matrizDePrueba)
print("MATRIZ CON PAISES Y AGUA ")
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
print(" LISTA DE SOLO PAISES: ")
print(" ")
print(listaPaisesAleatorios)
    #desordeno la lista para que la eleccion sea al azar
shuffle(listaPaisesAleatorios)
print(" ")
print(" LISTA DE PAISES MEZCLADOS PARA ASIGNARLOS AL AZAR: ")
print(" ")
print(listaPaisesAleatorios)

    
#funcion que divide la lista de paises de acuerdo a la cantidad de jugadores
def dividirLista(lista_paises, cantJug):
        if cantJug == 2:
            mitad = len(lista_paises)//2
            return (lista_paises[:mitad], lista_paises[mitad:])
        if cantJug == 3:
            div = len(lista_paises)//3
            return (lista_paises[:div], lista_paises[div:div*2], lista_paises[div*2:])
        if cantJug == 4:
            div = len(lista_paises)//4
            return (lista_paises[:div], lista_paises[div:div*2], lista_paises[div*2:div*3], lista_paises[div*3:])    


                

#funcion donde se ingresan la cantidad de jugadores para luego asignarle paises
def jugadorConPaises(cantPlayer):
    
    if cantPlayer == 2:
        listaPaisesJugador1, listaPaisesJugador2 = dividirLista(listaPaisesAleatorios,2)
        print(" ")
        print("lista paises jugador 1:")
        print(listaPaisesJugador1)
        print(" ")
        print("lista paises jugador 2:")
        print(listaPaisesJugador2) 
    if cantPlayer == 3:
        listaPaisesJugador1, listaPaisesJugador2, listaPaisesJugador3= dividirLista(listaPaisesAleatorios,3)
        print(" ")
        print("lista paises jugador 1:")
        print(listaPaisesJugador1)
        print(" ")
        print("lista paises jugador 2:")
        print(listaPaisesJugador2)
        print(" ")
        print("lista paises jugador 3:")
        print(listaPaisesJugador3)
    if cantPlayer == 4:
        listaPaisesJugador1, listaPaisesJugador2, listaPaisesJugador3, listaPaisesJugador4 = dividirLista(listaPaisesAleatorios,4)
        print(" ")
        print("lista paises jugador 1:")
        print(listaPaisesJugador1)
        print(" ")
        print("lista paises jugador 2:")
        print(listaPaisesJugador2)
        print(" ")
        print("lista paises jugador 3:")
        print(listaPaisesJugador3)    
        print(" ")
        print("lista paises jugador 4:")
        print(listaPaisesJugador4) 

#llamada a la funcion solo para revisar su funcionamiento
print("")
print("EJEMPLO PARA DOS JUGADORES: ")
jugadorConPaises(2)
print("")
print(("EJEMPLO PARA TRES JUGADORES:"))
jugadorConPaises(3)
print("")
print(("EJEMPLO PARA CUATRO JUGADORES:"))
jugadorConPaises(4)

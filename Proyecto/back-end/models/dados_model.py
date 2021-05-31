'''Esta clase se encarga de crear los objetos dados que se utilizan para ataques y defensas de los paises 
que posee cada jugador'''
import random
#Logica para lanzamiento de dados y determinar quien comienza la ronda
listaResultados = []

def determinarTurno(cantidadJugadores):
    #Lógica en una configuracion de 4 jugadores    
    if cantidadJugadores == 4:
        contador = 0
        
        while contador < cantidadJugadores:
            listaResultados.append(random.randint(1,6))
            contador = contador + 1
        print(listaResultados)
    else:
    #Lógica en una configuracion de 3 jugadores    
        if cantidadJugadores == 3:
            contador = 0
            while contador < cantidadJugadores:
                listaResultados.append(random.randint(1,6))
                contador = contador + 1
            print(listaResultados)
    #Identifico el MAYOR de la lista 
    mayor = max(listaResultados)
    #Identifico si el MAYOR se repite o no, para determinar si hay EMPATE
    hayEmpate = False
    
    if listaResultados.count(mayor) > 1:
        hayEmpate = True
        print("HAY EMPATE")
    else:
        hayEmpate = False
        print("NO HAY EMPATE")
        print("Primer turno: " + str(mayor))
        
#Si hay empate, debo desempatar para determinar quien comienza el juego
#Debo terminarla    
def desempatar():
    print("funcion desempate")

determinarTurno(3) #INVOCACION A LA FUNCION PARA VERIFICAR SI FUNCIONA SOLAMENTE
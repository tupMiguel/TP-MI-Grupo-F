from jugador_model import Jugador
from pais_model import Pais
class Juego:
    
    # creo una instancia del jugador 1
    j1 = Jugador('Fernando', 123)  
    # creo una instancia de pais, o sea un diccionario de paises vacio
    pais1j1 = Pais  
    # creo una instancia de pais, o sea un diccionario de paises vacio
    pais2j1 = Pais  
    #agrego al diccionario el pais y sus limites, que dependeran de los paises que se asignen en la matriz
    pais1j1 = {'Pais':'Argentina','Pais limitrofe 1':'Japon','Pais limitrofe 2':'Brasil'} 
    #agrego el pais con sus limites a la lista del jugador j1
    j1.add_pais(pais1j1) 
    #agrego al diccionario el pais y sus limites, que dependeran de los paises que se asignen en la matriz
    pais2j1 = {'Pais':'Brasil','Pais limitrofe 1':'Francia','Pais limitrofe 2':'Uruguay'}
    #agrego el pais con sus limites a la lista del jugador j1
    j1.add_pais(pais2j1)

    # creo una instancia del jugador 2
    j2 = Jugador('Miguel', 124)  
    # creo una instancia de pais, o sea un diccionario de paises vacio
    pais1j2 = Pais  
    # creo una instancia de pais, o sea un diccionario de paises vacio
    pais2j2 = Pais  
    #agrego al diccionario el pais y sus limites, que dependeran de los paises que se asignen en la matriz
    pais1j2 = {'Pais':'Francia','Pais limitrofe 1':'Africa','Pais limitrofe 2':'Italia'} 
    #agrego el pais con sus limites a la lista del jugador j1
    j2.add_pais(pais1j2) 
    #agrego al diccionario el pais y sus limites, que dependeran de los paises que se asignen en la matriz
    pais2j2 = {'Pais':'Alemania','Pais limitrofe 1':'Ingalterra','Pais limitrofe 2':'Portugal'}
    #agrego el pais con sus limites a la lista del jugador j1
    j2.add_pais(pais2j2)

    # creo una instancia del jugador 3
    j3 = Jugador('Javier', 125)  
    # creo una instancia de pais, o sea un diccionario de paises vacio
    pais1j3 = Pais  
    # creo una instancia de pais, o sea un diccionario de paises vacio
    pais2j3 = Pais  
    #agrego al diccionario el pais y sus limites, que dependeran de los paises que se asignen en la matriz
    pais1j3 = {'Pais':'Japon','Pais limitrofe 1':'Brasil','Pais limitrofe 2':'Australia'} 
    #agrego el pais con sus limites a la lista del jugador j1
    j3.add_pais(pais1j3) 
    #agrego al diccionario el pais y sus limites, que dependeran de los paises que se asignen en la matriz
    pais2j3 = {'Pais':'Africa','Pais limitrofe 1':'EEUU','Pais limitrofe 2':'Puerto Rico'}
    #agrego el pais con sus limites a la lista del jugador j1
    j3.add_pais(pais2j3)
    
    # creo una instancia del jugador 4
    j4 = Jugador('Lucia', 126)  
    # creo una instancia de pais, o sea un diccionario de paises vacio
    pais1j4 = Pais  
    # creo una instancia de pais, o sea un diccionario de paises vacio
    pais2j4 = Pais  
    #agrego al diccionario el pais y sus limites, que dependeran de los paises que se asignen en la matriz
    pais1j4 = {'Pais':'EEUU','Pais limitrofe 1':'Alemania','Pais limitrofe 2':'Mexico'} 
    #agrego el pais con sus limites a la lista del jugador j1
    j4.add_pais(pais1j4) 
    #agrego al diccionario el pais y sus limites, que dependeran de los paises que se asignen en la matriz
    pais2j4 = {'Pais':'Puerto Rico','Pais limitrofe 1':'Africa','Pais limitrofe 2':'Francia'}
    #agrego el pais con sus limites a la lista del jugador j1
    j4.add_pais(pais2j4)


    
    print "Nombre de jugador: ", j1.nombre
    print "ID jugador: ", j1.idplayer
    print "Paises asignados: "
    for n in j1.lista_paises:
        print n
    print " "

    print "Nombre de jugador: ", j2.nombre
    print "ID jugador: ", j2.idplayer
    print "Paises asignados: "
    for n in j2.lista_paises:
        print n    
    print " "

    print "Nombre de jugador: ", j3.nombre
    print "ID jugador: ", j3.idplayer
    print "Paises asignados: "
    for n in j3.lista_paises:
        print n
    print " "
        
    print "Nombre de jugador: ", j4.nombre
    print "ID jugador: ", j4.idplayer
    print "Paises asignados: "
    for n in j4.lista_paises:
        print n    


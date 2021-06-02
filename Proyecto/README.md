## Aclaración de desarrollo
Para facilitar el desarrollo de este proyecto se han creado dos Ramas en este repositorio, una donde se\
desarrollará el front-end y otra donde se desarrollara el back-end. Cuando sea el momento de hacer un release de la versión 1
ambas se mergearan a la rama main.

# Proyecto: Juego inspirado en T.E.G
# Grupo F - Turno TARDE

## Integrantes:
- `Angeloni, Agustina`
- `Cabrera, Fernando`
- `Condori, Miguel`
- `Cortinez, Juan`
- `Gauna, Javier`
- `Scripponi, Lucía`

## PROYECTO ELEGIDO
Se plantea un videojuego inspirado en el famoso juego de mesa T.E.G.\
IDEA GENERAL El juego propone un conflicto bélico que tiene lugar sobre un mapa dividido de forma matricial. Para empezar,\
un jugador tendrá la posibilidad de editar el mapa en el cual se jugará, creando distintos sectores y conexiones, esto\
permitirá que cada partida sea diferente a la anterior y que se pueda variar la dinámica del mapa.


Se plantea una arquitectura cliente - servidor donde los distintos clientes\
(jugadores) se conectan mediante sockets para poder tener datos de la\
partida en tiempo real. Para poder realizar el servidor se utilizará Python y\
para realizar el cliente se usará el framework Angular que utiliza typescript.\
Se utilizará esta tecnología ya que Angular facilita muchísimo la utilización\
del patrón modular para los distintos componentes que formarán el sistema\
y tiene una optimización muy buena del renderizado dinámico de datos.

Para editar código se utilizará VS CODE\
para el back end se utilizará python 3.9.4 con el micro framework Flask\
para el front se utilizará typeScript con el framework Angular 11
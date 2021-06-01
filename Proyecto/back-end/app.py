from controllers.partida_controller import *
from models.jugador_model import JugadorModel
from models.pais_model import PaisModel
from models.partida_model import PartidaModel

from services.baseDeDatos_service import BaseDeDatosService

import json

partidaController = PartidaController();

# # # # # # # # # Instancia de una partida para hacer pruebas # # # # # # # # # # # # # # 
jugador1 = JugadorModel('id1gsadw', 'riki');
jugador2 = JugadorModel('id23asdasd', 'pepe');
jugador3 = JugadorModel('id9sdsanbi', 'juan');
jugador4 = JugadorModel('id23nlkjn', 'hongito');

pais1 = PaisModel('argentina', 'id1gsadw', False);
pais2 = PaisModel('colombia', 'id23asdasd', False);
pais3 = PaisModel('venezuela', 'id23nlkjn', True);
pais4 = PaisModel('ecuador', 'id23nlkjn', True);

partida = PartidaModel('idJuego1231', True, [jugador1, jugador2, jugador3, jugador4], [[pais1, pais2], [pais3, pais4]], 20);
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


partidaController.ataque('id1gsadw', 0, 1, partida);

matriz = partidaController.colocarPaises([[0,1],[1,0]]) #probando método para colocar paises en pequenia matriz de prueba de 2x2
print(matriz)

#print(partida.__dict__);
# baseDeDatos.add_data(str(partida.__dict__));
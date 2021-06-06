import json

from controllers.partida_controller import *
from models.jugador_model import JugadorModel
from models.pais_model import PaisModel
from models.partida_model import PartidaModel

from services.baseDeDatos_service import BaseDeDatosService



partidaController = PartidaController()

baseDeDatosService = BaseDeDatosService()

# # # # # # # # # Instancia de una partida para hacer pruebas # # # # # # # # # # # # # # 
jugador1 = JugadorModel('id1gsadw', 'riki')
jugador2 = JugadorModel('id23asdasd', 'pepe')
jugador3 = JugadorModel('id9sdsanbi', 'juan')
jugador4 = JugadorModel('id23nlkjn', 'hongito')

pais1 = PaisModel('argentina', 'id1gsadw', False)
pais2 = PaisModel('colombia', 'id23asdasd', False)
pais3 = PaisModel('venezuela', 'id23nlkjn', True)
pais4 = PaisModel('ecuador', 'id23nlkjn', True)

partida = PartidaModel('idJueg11', True, [jugador1, jugador2, jugador3, jugador4], [[pais1, pais2], [pais3, pais4]], 20)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

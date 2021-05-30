from controllers.partida_controller import PartidaController
from models.jugador_model import JugadorModel
from models.pais_model import PaisModel
from models.partida_model import PartidaModel

from services.baseDeDatos_service import BaseDeDatosService

import json

partidaController = PartidaController();

# # # # # # # # # Instancia de una partida para hacer pruebas # # # # # # # # # # # # # # 
jugador1 = JugadorModel("id1gsadw", "riki");
jugador2 = JugadorModel("id23asdasd", "pepe");
jugador3 = JugadorModel("id9sdsanbi", "juan");
jugador4 = JugadorModel("id23nlkjn", "hongito");

pais1 = PaisModel("argentina", "id1gsadw", False);
pais2 = PaisModel("colombia", "id23asdasd", False);
pais3 = PaisModel("", "", True);
pais4 = PaisModel("", "", True);

partida = PartidaModel("idJuego1231", True, [jugador1, jugador2, jugador3, jugador4], [[pais1, pais2], [pais3, pais4]]);
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


partidaController.ataque("id1gsadw", 0, 1, partida);

# print(partida.__dict__);
# baseDeDatos.add_data(str(partida.__dict__));
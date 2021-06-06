from services.baseDeDatos_service import BaseDeDatosService
from models.jugador_model import JugadorModel


class JugadorController:
    bbdd = BaseDeDatosService()

    def puede_atacar(self, jugador: JugadorModel) -> bool:
        """
        Indica si un jugador cumple los requisitos para atacar
        
        :param jugador: JugadorModel
        :return: bool
        """

        if jugador.dados_ataque >= 1:
            return True
        return False

    def ha_perdido(self, jugador: JugadorModel):
        """
        Indica si un jugador ha perdido en la partida

        :param jugador: JugadorModel
        :return: bool
        """
        pass
        # todo


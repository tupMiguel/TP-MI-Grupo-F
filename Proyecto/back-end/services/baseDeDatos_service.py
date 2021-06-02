class BaseDeDatosService:
 
    __instancia = None
    
    __indexado = {}

    filePath = "Proyecto/back-end/storage/partidas.txt"
    
    #Singleton
    def __new__(self):
        if self.__instancia is None:
           self.__instancia= object.__new__(self)
           self.__indexate_database(self)
        return self.__instancia
    
    # __indexate_database()
    # lee todas las partidas en la base de datos y rellena el atributo indexado utilizando como key el id de la partida y como value la línea
    # del partidas.txt en donde se encuentra dicha partida. Este método se ejecuta en el constructor de la clase
    # @params
    # @return
    def __indexate_database(self):
        file = open(self.filePath, "r")
        partidas = file.readlines()
        file.close()
        # itero en todas las partidas de la base de datos y voy indexandolas por el atributo idJuego
        for index, partida in enumerate(partidas):
            self.__indexado[partida[13:21]] = index
        return

    # search_partida_by_id()
    # Busca una partida 
    # @params
    # @return
    def search_partida_by_id(self, idPartida: str):
        file = open(self.filePath, "r")
        positionInTxt = self.__indexado[idPartida]
        partidaEncontrada = file.readlines()[positionInTxt : positionInTxt+1][0]
        print(partidaEncontrada)
        file.close()
        return partidaEncontrada


    # save_partida()
    # Guarda una partida en la base de datos e indexa su id en el atributo __indexado
    # @params data ---> partida a guardar
    # @return
    def save_partida(self, partida: str):
        file = open(self.filePath, "a")
        file.write(partida + "\n")
        file.close()
        # agrego el id de partida al indexado
        self.__indexado[partida[13:21]] = self.__indexado[list(self.__indexado)[-1]] + 1
        print(self.__indexado)
        return

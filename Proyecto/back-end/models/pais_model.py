import json

class PaisModel:
    def __init__(self, nombre: str, duenioId: str, agua: bool):
        self.nombre = nombre
        self.duenioId = duenioId
        self.agua = agua
    
    def __repr__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
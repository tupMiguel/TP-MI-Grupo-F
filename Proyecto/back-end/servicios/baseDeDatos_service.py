from dataclasses import dataclass

import os

@dataclass
class BaseDeDatosService:
 
    __instancia=None
    
    #Singleton
    def __new__(cls):
        if cls.__instancia is None:
           cls.__instancia= object.__new__(cls)
        return cls.__instancia
    
    filePath = os.path.relpath('partidas.txt')
    file = open(filePath, "a")

    # def create_txt(self, file_name):
    #     self.file.write("Primera linea \n")
    #     self.file.close()
    #     return

    def add_data(self, data):
        self.file.write(data + "\n")
        self.file.close()
        return
   
    file = open(filePath, "r")

     #Lectura de String del archivo
    def read_data(self, num=0):
        lineas=self.archivo.readlines()
        frase=lineas[num]
        print(frase)
        return frase

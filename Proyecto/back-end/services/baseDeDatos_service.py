from dataclasses import dataclass

import os

@dataclass
class BaseDeDatosService:

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

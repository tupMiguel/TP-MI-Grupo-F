import os

# Crea un archivo .txt
# @params file_name
class storageService():
    
    def create_txt(file_name):
        filePath = os.path.relpath('storage/'+file_name+'.txt')
        file = open(filePath, "w")
        file.write("Primera linea")
        file.close()
        return
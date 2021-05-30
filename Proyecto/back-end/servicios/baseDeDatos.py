import os

class BaseDeDatos():
    
    __instancia=None
    
    #Singleton
    def __new__(cls):
        if cls.__instancia is None:
           cls.__instancia= object.__new__(cls)
        return cls.__instancia
    
    #Agrego String al archivo
    def guardarString(self, linea):
        archivo=open("/back-end/storage/storage.txt ","a") 
        archivo.write("\n"+linea)
        archivo.close()

    #Lectura de String del archivo
    def leerString(self, num=0):
        archivo=open("/back-end/storage/storage.txt ","r") 
        lineas=archivo.readlines()
        frase=lineas[num]
        print(frase)
        return frase

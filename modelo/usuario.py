class Usuario:
    def __init__(self,run="",nombre="",apellido=""):
        self.__run = run
        self.__nombre = nombre
        self.__apellido =apellido
#Setters
    def setRun(self, run):
        self.__run = run

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido
#Getters
    def getRun(self):
        return self.__run

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido
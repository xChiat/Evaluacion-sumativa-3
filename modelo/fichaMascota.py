from modelo.mascota import Mascota
class FichaMascota:
    def __init__(self,idFicha=None,mascota=Mascota()):
        self.__idFicha = idFicha
        self.__mascota = mascota
#Str de clase
    def __str__(self):
        return f"Id Ficha: {self.__idFicha} Mascota: {self.__mascota}"
#Setters
    def setIdFicha(self,idFicha):
        self.__idFicha = idFicha
    def setMascota(self,mascota):
        self.__mascota = mascota
#Getters
    def getIdFicha(self):
        return self.__idFicha
    def setMascota(self):
        return self.__mascota
from modelo.usuario import Usuario
class Resepcionista(Usuario):
    def __init__(self,run="",nombre="",apellido="",clave=""):
        super().__init__(run,nombre,apellido)
        self.__clave =clave
#String de Clase
    def __str__(self):
        return f"{super().__str__()}"
#Setters
    def setRun(self,run):
        super().setRun(run)
    def setNombre(self,nombre):
        super().setNombre(nombre)
    def setApellido(self, apellido):
        super().setApellido(apellido)
    def setclave(self,clave):
        self.__clave =clave
#Getters
    def getRun(self):
        return super().getRun()
    def getNombre(self):
        return super().getNombre()
    def getApellido(self):
        return super().getApellido()
    def getClave(self):
        return self.__clave
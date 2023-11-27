from modelo.cliente import Cliente
class Mascota:
    # lista
    __lista = []
    def __init__(self,idMascota=None,nombre="",edad=0,tipoMascota="",cliente=""):
       self.__idMascota = idMascota
       self.__nombre = nombre
       self.__edad = edad
       self.__tipoMascota = tipoMascota
       self.__cliente = cliente

#Setters
    def setIdMascota(self,idMascota):
        self.__idMascota = idMascota
    def setNombMascota(self,nombre):
        self.__nombre = nombre
    def setEdad(self,edad):
        self.__edad = edad
    def setTipoMascota(self,tipoMascota):
        self.__tipoMascota = tipoMascota
#Getters
    def getIdMascota(self):
        return self.__idMascota
    def getNombMascota(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getTipoMascota(self):
        return self.__tipoMascota
    def getCliente(self):
        return self.__cliente
    def getListaMascota(self):
        return self.__lista
    
    #Prepare lista
    def prepareMascota(self, lista):
        for msc in lista:
            self.__lista.append(msc)
            
    #Encontrar en lista
    def buscarMascota(self, idMascota):
        for msc in self.getListaMascota():
            if msc.getIdMascota() == idMascota:
                return msc
        return None
    
    #Limpiar lista
    def clearLista(self):
        self.__lista.clear()


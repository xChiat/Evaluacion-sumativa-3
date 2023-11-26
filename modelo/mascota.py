from modelo.cliente import Cliente
class Mascota:
    __listaMascota = []
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
        return self.__listaMascota
#Precarga
    def prepareMascota(self, listDB):
            for msc in listDB:
                self.__listarMascota.append(msc)
#Encontrar en lista
    def buscarMascota(self, idMascota):
        mascota = self.getListaMascota()
        for msc in mascota:
            if self.getIdMascota() == idMascota:
                return msc
        return None
#Limpiar lista
    def clearLista(self):
        self.__listarMascota.clear()
#Modificar lista
    def modNomb(self,idMascota,nomb):
        mascota = self.getListaMascota()
        msc = self.buscarMascota(idMascota)
        if nomb is not None:
            mascota[msc+1] = nomb
    def modEdad(self,idMascota,edad):
        mascota = self.getListaMascota()
        msc = self.buscarMascota(idMascota)
        if edad is not None:
            mascota[msc+2] = edad
    def modTipoMascota(self,idMascota,nomb):
        mascota = self.getListaMascota()
        msc = self.buscarMascota(idMascota)
        if nomb is not None:
            mascota[msc+3] = nomb
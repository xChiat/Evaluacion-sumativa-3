from modelo.mascota import Mascota
from dao.dao_mascota import MascotaDAO
class MascotaDTO:
    def prepareMascota(self):
        daoMasc = MascotaDAO()
        result = daoMasc.prepareMascota()
        lista = []
        if result is not None:
            for msc in result:
                mascota = Mascota(idMascota = msc[0], tipoMascota = msc[1], nombMascota=msc[2], edad=msc[3])
                lista.append(mascota)
        Mascota().prepareMascota(lista)
    
    #Limpia la lista Cargo y la carga nuevamente. 
    def syncListaMascota(self):
        Mascota().clearLista()
        self.prepareCliente()
        
    #Buscar todos los clientes
    def listarClientes(self):
        mascota = Mascota().getLista()
        return mascota
    
    #Busca un cargo en la lista de clase
    def buscarCliente(self, idMascota):
        mascota = Mascota()
        result = mascota.buscarMascota(idMascota)
        if result is None:
            return None
        else:
            return result

    #Agregar cargos
    def addCliente(self, idMascota,nombMascota,edad,tipoMascota):
        daoMasc = MascotaDAO()
        resultado = daoMasc.addCliente(Mascota(idMascota=idMascota,nombMascota=nombMascota,edad=edad,tipoMascota=tipoMascota))
        self.syncListaMascota()
        return resultado
    
    #Eliminar cargos
    def delCliente(self, idMascota):
        daoMasc = MascotaDAO()
        resultado = daoMasc.delCliente(Mascota(idMascota=idMascota))
        self.syncListaMascota()
        return resultado
    
    #Modificar cargos
    def updateCliente(self, idMascota,nombMascota,edad,tipoMascota):
        daoMasc = MascotaDAO()
        resultado = daoMasc.updateCliente(Mascota(idMascota=idMascota,nombMascota=nombMascota,edad=edad,tipoMascota=tipoMascota))
        self.syncListaMascota()
        return resultado
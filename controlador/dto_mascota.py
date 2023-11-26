from modelo.mascota import Mascota
from dao.dao_mascota import MascotaDAO
class MascotaDTO:
    def prepareMascota(self):
        daoMasc = MascotaDAO()
        result = daoMasc.prepareMascota()
        lista = []
        if result is not None:
            for msc in result:
                type = ""
                if msc[1]==1:
                    type = "Perro"
                    return type
                elif msc[1]==2:
                    type = "Gato"
                    return type
                mascota = Mascota(idMascota = msc[0], tipoMascota = type, nombMascota=msc[2], edad=msc[3])
                lista.append(mascota)
        Mascota().prepareMascota(lista)
    
    #Limpia la lista Cargo y la carga nuevamente. 
    def syncListaMascota(self):
        Mascota().clearLista()
        self.prepareCliente()
        
    #Buscar todos los clientes
    def listarMascotas(self):
        mascota = Mascota().getLista()
        return mascota
    
    #Busca un cargo en la lista de clase
    def buscarMascota(self, idMascota):
        mascota = Mascota()
        result = mascota.buscarMascota(idMascota)
        if result is None:
            return None
        else:
            return result

    #Agregar cargos
    def addMascota(self, idMascota, nombre, edad, tipo, cliente):
        daoMascota = MascotaDAO()
        # Agregar la mascota a la base de datos y obtener el resultado
        result = daoMascota.addMascota(Mascota(idMascota=idMascota, nombre=nombre, edad=edad, tipoMascota=tipo, cliente=cliente))
        return result
    
    #Eliminar cargos
    def delMascota(self, idMascota):
        daoMasc = MascotaDAO()
        resultado = daoMasc.delMascota(Mascota(idMascota=idMascota))
        self.syncListaMascota()
        return resultado
    
    #Modificar cargos
    def updateMascota(self, idMascota,nombMascota,edad,tipoMascota):
        daoMasc = MascotaDAO()
        resultado = daoMasc.updateMascota(Mascota(idMascota=idMascota,nombMascota=nombMascota,edad=edad,tipoMascota=tipoMascota))
        self.syncListaMascota()
        return resultado
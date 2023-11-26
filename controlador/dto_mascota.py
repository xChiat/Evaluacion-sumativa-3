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
                if msc[1] == 1:
                    type = "Perro"
                elif msc[1] == 2:
                    type = "Gato"
                mascota = Mascota(idMascota=msc[0], tipoMascota=type, nombre=msc[2], edad=msc[3])
                lista.append(mascota)
        Mascota().prepareMascota(lista)
    
    #Limpia la lista Cargo y la carga nuevamente. 
    def syncListaMascota(self):
        Mascota().clearLista()
        self.prepareMascota()
        
    #Buscar todos los clientes
    def listarMascotas(self):
        mascota = Mascota().getListaMascota()
        for msc in mascota:
            print(f"ID Mascota: {msc.getIdMascota()} Nombre: {msc.getNombMascota()} Edad: {msc.getEdad()} Tipo de Mascota: {msc.getTipoMascota()}")
        
    
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
        result = daoMascota.addMascota(Mascota(idMascota=idMascota,nombre=nombre, edad=edad, tipoMascota=tipo, cliente=cliente))
        self.syncListaMascota()
        return result
    
    #Eliminar cargos
    def delMascota(self, idMascota):
        daoMasc = MascotaDAO()
        resultado = daoMasc.delMascota(Mascota(idMascota=idMascota))
        self.syncListaMascota()
        return resultado
    
    #Modificar cargos
    def updateMascota(self, idMascota,nombMascota,edad,tipoMascota):
        mascota = self.buscarMascota(idMascota)
        if mascota is None:
            return "El Cliente no existe, no puedes modificarlo."
        daoMascota = MascotaDAO()
        if nombMascota != '':
            mascota.setNombMascota(nombMascota)
        if edad != '':
            mascota.setEdad(edad)
        if tipoMascota != '':
            mascota.setTipoMascota(tipoMascota)
        resultado = daoMascota.updateMascota(mascota)
        return resultado
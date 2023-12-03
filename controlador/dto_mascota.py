from modelo.mascota import Mascota
from modelo.cliente import Cliente
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
                mascota = Mascota(idMascota=msc[0], tipoMascota=type, nombre=msc[2], edad=msc[3], cliente=Cliente(run=msc[4],nombre=msc[5], apellido=msc[6], telefono= msc[7],correo= msc[8]))
                lista.append(mascota)
        Mascota().prepareMascota(lista)
    
    def syncListaMascota(self):
        Mascota().clearLista()
        self.prepareMascota()

    def listarMascotas(self):
        mascota = Mascota().getListaMascota()
        return mascota
    
    def buscarMascota(self, idMascota):
        mascota = Mascota()
        result = mascota.buscarMascota(idMascota)
        if result is None:
            return None
        else:
            return result

    def addMascota(self, idMascota, nombre, edad, tipo, rut):
        daoMascota = MascotaDAO()
        result = daoMascota.addMascota(Mascota(idMascota=idMascota,nombre=nombre, edad=edad, tipoMascota=tipo, cliente=Cliente(run=rut)))
        self.syncListaMascota()
        return result

    def delMascota(self, idMascota):
        daoMasc = MascotaDAO()
        resultado = daoMasc.delMascota(Mascota(idMascota=idMascota))
        self.syncListaMascota()
        return resultado

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
    
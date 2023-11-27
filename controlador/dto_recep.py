from utils.encoder import Encoder
from modelo.recepcionista import Resepcionista
from dao.dao_recep import RecepcionistaDAO

class RecepcionistaDTO():
    
    def autenticaRecepcionista(self, run, password):
        daoRecep = RecepcionistaDAO()
        resultado = daoRecep.autenticaRecepcionista(Resepcionista(run=run, clave=Encoder().encode(password)))
        return Resepcionista(resultado[0]) if resultado is not None else None
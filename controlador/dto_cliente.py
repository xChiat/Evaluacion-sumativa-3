from modelo.cliente import Cliente
from dao.dao_cliente import ClienteDAO
class ClienteDTO:
    def prepareCliente(self):
        daoCli = ClienteDAO()
        result = daoCli.prepareCliente()
        lista = []
        if result is not None:
            for cli in result:
                cliente = Cliente(run = cli[0], nombre = cli[1], apellido=[2], telefono=[3], correo=[4])
                lista.append(cliente)
        Cliente().prepareCliente(lista)
    
    #Limpia la lista Cargo y la carga nuevamente. 
    def syncListaCliente(self):
        Cliente().clearLista()
        self.prepareCliente()
        
    #Buscar todos los clientes
    def listarClientes(self):
        cliente = Cliente().getLista()
        return cliente
    
    #Busca un cargo en la lista de clase
    def buscarCliente(self, run):
        cliente = Cliente()
        result = cliente.buscarCliente(run)
        if result is None:
            return None
        else:
            return result

    #Agregar cargos
    def addCliente(self, run, nombre, apellido, telefono, correo):
        daoCli = ClienteDAO()
        resultado = daoCli.addCliente(Cliente(run=run, nombre=nombre, apellido=apellido, telefono=telefono, correo=correo))
        self.syncListaCliente()
        return resultado
    
    #Eliminar cargos
    def delCliente(self, run):
        daoCli = ClienteDAO()
        resultado = daoCli.delCliente(Cliente(run=run))
        self.syncListaCliente()
        return resultado
    
    #Modificar cargos
    def updateCliente(self, run, nombre, apellido, telefono, correo):
        daoCli = ClienteDAO()
        resultado = daoCli.updateCliente(Cliente(run=run, nombre=nombre, apellido=apellido, telefono=telefono, correo=correo))
        self.syncListaCliente()
        return resultado
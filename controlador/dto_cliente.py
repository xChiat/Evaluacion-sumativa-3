from modelo.cliente import Cliente
from dao.dao_cliente import ClienteDAO
from controlador.dto_mascota import MascotaDTO
class ClienteDTO:
    def prepareCliente(self):
        daoCli = ClienteDAO()
        result = daoCli.prepareCliente()
        lista = []
        if result is not None:
            for cli in result:
                cliente = Cliente(run=cli[0], nombre=cli[1], apellido=cli[2], telefono=cli[3], correo=cli[4])
                lista.append(cliente)
        Cliente().prepareCliente(lista)
    
    #Limpia la lista cliente y la carga nuevamente. 
    def syncListaCliente(self):
        Cliente().clearLista()
        self.prepareCliente()
        
    #Buscar todos los clientes
    def listarClientes(self):
        cliente = Cliente().getLista()
        return cliente
    
    #Busca un cliente en la lista de clase
    def buscarCliente(self, run):
        cliente = Cliente()
        result = cliente.buscarCliente(run)
        if result is None:
            return None
        else:
            return result

    #Agregar cliente
    def agregarCliente(self, run, nombre, apellido, telefono, correo):
        daoCli = ClienteDAO()
        cliente = Cliente(run=run, nombre=nombre, apellido=apellido, telefono=telefono, correo=correo)
        resultado = daoCli.agregarCliente(cliente)
        self.syncListaCliente()
        return resultado
    
    #Eliminar cliente
    def eliminarCliente(self, run):
        daoCli = ClienteDAO()
        resultado = daoCli.eliminarCliente(Cliente(run=run))
        self.syncListaCliente()
        MascotaDTO.syncListaMascota()
        return resultado
    
    #Modificar cliente
    def modificarCliente(self, run, nombre, apellido, telefono, correo):
        cliente = self.buscarCliente(run)
        if cliente is None:
            return "El Cliente no existe, no puedes modificarlo."
        daoCli = ClienteDAO()
        if nombre != '':
            cliente.setNombre(nombre)
        if apellido != '':
            cliente.setApellido(apellido)
        if telefono != '':
            cliente.setTelefono(telefono)
        if correo != '':
            cliente.setCorreo(correo)
        resultado = daoCli.modificarCliente(cliente)
        return resultado

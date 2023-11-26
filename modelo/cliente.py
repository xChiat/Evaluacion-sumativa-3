from modelo.usuario import Usuario
class Cliente(Usuario):
    __listaCliente = []
    def __init__(self,run="",nombre="",apellido="",telefono="",correo=""):
        super().__init__(run,nombre,apellido)
        self.__telefono = telefono
        self.__correo = correo
        self.getLista().append(self)
#String de clase
    def __str__(self):
        return f"RUN: {self.getRun()} Nombre: {self.getNombre()} Apellido: {self.getApellido()} Telefono: {self.__telefono} Correo: {self.__correo}"
#Setters
    def setRun(self,run):
        super().setRun(run)
    def setNombre(self,nombre):
        super().setNombre(nombre)
    def setApellido(self, apellido):
        super().setApellido(apellido)
    def setTelefono(self,telefono):
        self.__telefono = telefono
    def setCorreo(self,correo):
        self.__correo = correo
#Getters
    def getTelefono(self):
        return self.__telefono
    def getCorreo(self):
        return self.__correo
    def getRun(self):
        return super().getRun()
    def getNombre(self):
        return super().getNombre()
    def getApellido(self):
        return super().getApellido()
    
    #@classmethod
    def prepareCliente(cls, lista):
        cls.__listaCliente = lista

    #@classmethod
    def getLista(cls):
        return cls.__listaCliente

    #@classmethod
    def clearLista(cls):
        cls.__listaCliente.clear()  
                      
#Encontrar en lista
    def buscarCliente(self, run):
        for cli in self.getLista():
            if cli.getRun() == run:
                return cli
        return None
    
#Modificar lista
    def modNombre(self,run, nomb):
        cliente = self.getLista()
        cli = self.buscarCliente(run)
        if nomb is not None:
            cliente[cli+1] = nomb
    def modApellido(self,run, apll):
        cliente = self.getLista()
        cli = self.buscarCliente(run)
        if apll is not None:
            cliente[cli+2] = apll
    def modTelefono(self,run,tlf):
        cliente = self.getLista()
        cli = self.buscarCliente(run)
        if tlf is not None:
            cliente[cli+3] = tlf
    def modCorreo(self,run,crr):
        cliente = self.getLista()
        cli = self.buscarCliente(run)
        if crr is not None:
            cliente[cli+4] = crr
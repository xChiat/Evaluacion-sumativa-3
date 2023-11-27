from modelo.usuario import Usuario
class Cliente(Usuario):
    # lista
    __lista = []
    def __init__(self,run="",nombre="",apellido="",telefono="",correo=""):
        super().__init__(run,nombre,apellido)
        self.__telefono = telefono
        self.__correo = correo

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
    def getLista(self):
        return self.__lista
    
    #Prepare lista
    def prepareCliente(self, lista):
        for cli in lista:
            self.__lista.append(cli)

    #Encontrar en lista
    def buscarCliente(self, run):
        for cli in self.getLista():
            if cli.getRun() == run:
                return cli
        return None
    
    #Limpiar lista
    def clearLista(self):
        self.__lista.clear()  
                      
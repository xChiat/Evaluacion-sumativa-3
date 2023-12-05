from controlador.dto_recep import RecepcionistaDTO
from controlador.dto_cliente import ClienteDTO
from controlador.dto_mascota import MascotaDTO

# CARGA DE DATOS
def cargaInicial():
    ClienteDTO().prepareCliente()
    MascotaDTO().prepareMascota()

#-------- VALIDAR INT Y STR -----------
def validaInt(txt):
    while True:
        try:
            opc = int(input(f"Ingresa {txt}: "))
            return opc
        except:
            print("Error de Ingreso, solo puedes ingresar números.")
            
def validaStr(txt):
    while True:
        valor = input(f"Ingrese {txt}: ").strip()
        if valor:
            return valor
        else:
            print("Campo incorrecto, no debe estar vacío.")

# ---------- CLIENTE ----------
def validateFindAllClientes():
    print("\n--------------------")
    print("Listado de Clientes.")
    print("--------------------\n")
    print("")
    result = ClienteDTO().listarClientes()
    if len(result) > 0:
        for cli in result:
            print(cli)
    else:
        print("No hay Clientes Registrados.")
        
def validateBuscarCliente(run):
    result = ClienteDTO().buscarCliente(run)
    if result is None:
        return None
    else:
        return result
    
def validateEliminarCliente():
    print("\n--------------------")
    print("Eliminar Cliente.")
    print("--------------------\n")
    run = validaStr("un RUT")
    val = validateBuscarCliente(run)
    if val is None:
        return print("El Cliente no existe, no se puede Eliminar.")
    else:
        print("¿Estas seguro que deseas eliminar al Cliente?")
        confirm = input("Presiona Y/y para Confirmar o N/n para Cancelar:")
        confirm = confirm.upper()
        if confirm == "Y":
            result = ClienteDTO().eliminarCliente(run)
            return print(result)
        elif confirm == "N":
            return print("Operación Cancelada.")
        else:
            print("Opción invalida, intentalo nuevamente.")
            return validateEliminarCliente()    
        
def validateAgregarCliente():
    print("\n--------------------")
    print("Agregar Cliente.")
    print("--------------------\n")
    run = validaStr("un RUT")
    val = validateBuscarCliente(run)
    if val is not None:
        return print("El RUT del Cliente ya existe, no puedes volver a registrarlo.")
    else:
        nombre = validaStr("Nombre del Cliente")
        apellido = validaStr("Apellido del Cliente")
        correo = validaStr("Correo del Cliente")
        telefono = validaStr("Teléfono del Cliente")
        if not nombre or not apellido or not correo or not telefono:
            return print("Todos los campos son requeridos. Operación Cancelada.")
        else:
            result = ClienteDTO().agregarCliente(run, nombre, apellido, telefono, correo)
            print(result)

def validateModificarCliente():
    print("\n--------------------")
    print("Modificar Cliente.")
    print("--------------------\n")
    run = validaStr("el RUT")
    val = validateBuscarCliente(run)
    if val is None:
        return print("El Cliente no existe, no puedes modificarlo.")
    else:
        print("Pulse enter si no desea modificar algún campo.")
        nombre = input("Ingrese el nuevo Nombre: ")
        apellido = input("Ingrese el nuevo Apellido: ")
        telefono = input("Ingrese el nuevo teléfono: ")
        correo = input("Ingrese el nuevo Correo: ")
        if nombre or apellido or telefono or correo:
            result = ClienteDTO().modificarCliente(run, nombre, apellido, telefono, correo)
            print(result)
        else:
            print("Ningún campo ingresado para modificar.")
            
            
#---------- MASCOTAS -----------
def validateFindAllMascotas():
    print("\n--------------------")
    print("Listado de Mascotas.")
    print("--------------------\n")
    print("")
    result = MascotaDTO().listarMascotas()
    if len(result) > 0:
        for msc in result:
            print(msc)
    else:
        print("No hay Mascotas Registradas.")

def validateBuscarMascota(idMascota):
    result = MascotaDTO().buscarMascota(idMascota)
    if result is None:
        return None
    else:
        return result 

def validateEliminarMascota():
    print("\n--------------------")
    print("Eliminar Mascota.")
    print("--------------------\n")
    idMascota = validaInt(" el id de la Mascota")
    val = validateBuscarMascota(idMascota)
    if val is None:
        return print("La Mascota no existe, no se puede Eliminar.")
    else:
        print("¿Estas seguro que deseas eliminar a la Mascota?")
        confirm = input("Presiona Y/y para Confirmar o N/n para Cancelar:")
        confirm = confirm.upper()
        if confirm == "Y":
            result = MascotaDTO().eliminarMascota(idMascota)
            return print(result)
        elif confirm == "N":
            return print("Operación Cancelada.")
        else:
            print("Opción invalida, intentalo nuevamente.")
            return validateEliminarMascota()

def validateAgregarMascota():
    print("\n--------------------")
    print("Agregar Mascota.")
    print("--------------------\n")
    run = validaStr("RUT del Cliente")
    cliente_existente = validateBuscarCliente(run)

    if cliente_existente is None:
        return print("El Cliente no existe. Operación Cancelada.")
    else:
        idMascota = validaInt("el id de la mascota")
        val = validateBuscarMascota(idMascota)
        if val is not None:
            return print("La mascota ya existe, no puedes volver a agregarla")
        else:
            nombre = validaStr("el Nombre de la Mascota")
            edad = validaInt("Edad de la Mascota")
            tipo = validaInt("Selecciona la opcion de tu tipo de Mascota 1: Perro  2:Gato")
            if not nombre or not edad or not tipo:
                return print("Todos los campos son requeridos. Operación Cancelada.")
            else:
                if tipo == 1:
                    perro = "Perro"
                    result = MascotaDTO().agregarMascota(idMascota, nombre, edad, perro, run)
                    print(result)
                elif tipo == 2:
                    gato = "Gato"
                    result = MascotaDTO().agregarMascota(idMascota, nombre, edad, gato, run)
                    print(result)
                else:
                    return print("Escoja un tipo de Mascota Valido")

def validateModificarMacota():
    print("\n--------------------")
    print("Modificar Mascota.")
    print("--------------------\n")
    idMascota = validaInt("el ID de la mascota")
    val = validateBuscarMascota(idMascota)

    if val is None:
        print("La mascota no existe, no se puede modificar.")
        return
    else:
        print(f"\nModificando datos de la mascota con ID: {idMascota}")
        print("Presiona Enter si no deseas modificar algún campo.")
        nombre = str(input("Ingrese el nuevo Nombre de la Mascota : "))
        edad = input("Ingrese la nueva Edad de la Mascota : ")
        tipoMascota = input("Selecciona la opcion de tu tipo de Mascota 1: Perro  2:Gato :")
        run = str(input("Ingrese el RUN del nuevo dueño : "))
        cliente_existente = validateBuscarCliente(run)
        if edad != "":
            edadmsc = validaInt(edad)
            if cliente_existente is not None or run == "":
                if nombre or edad or tipoMascota or run:
                    if tipoMascota == "1":
                        perro = "Perro"
                        result = MascotaDTO().modificarMacota(idMascota, nombre, edadmsc, perro, run)
                        print(result)
                    elif tipoMascota == "2":
                        gato = "Gato"
                        result = MascotaDTO().modificarMacota(idMascota, nombre, edadmsc, gato, run)
                        print(result)
                    elif tipoMascota == "":
                        result = MascotaDTO().modificarMacota(idMascota, nombre, edadmsc, tipoMascota, run)
                        print(result)
                    else:
                        return print("Escoja un tipo de Mascota Valido")
                else:
                    print("Ningún campo ingresado para modificar.")
            else:
                print("El cliente no existe por lo tanto no puede ser el nuevo dueño.")
                print("Solo seran modificados el resto de campos.")
                if nombre or edad or tipoMascota:
                    result = MascotaDTO().modificarMacota(idMascota, nombre, edad, tipoMascota, "")
                    print(result)
                else:
                    print("Ningún campo ingresado para modificar.")
        elif edad == "":
            if cliente_existente is not None or run == "":
                if nombre or edad or tipoMascota or run:
                    if tipoMascota == "1":
                        perro = "Perro"
                        result = MascotaDTO().modificarMacota(idMascota, nombre, edad, perro, run)
                        print(result)
                    elif tipoMascota == "2":
                        gato = "Gato"
                        result = MascotaDTO().modificarMacota(idMascota, nombre, edad, gato, run)
                        print(result)
                    elif tipoMascota == "":
                        result = MascotaDTO().modificarMacota(idMascota, nombre, edad, tipoMascota, run)
                        print(result)
                    else:
                        return print("Escoja un tipo de Mascota Valido")
                else:
                    print("Ningún campo ingresado para modificar.")
            else:
                print("El cliente no existe por lo tanto no puede ser el nuevo dueño.")
                print("Solo seran modificados el resto de campos.")
                if nombre or edad or tipoMascota:
                    result = MascotaDTO().modificarMacota(idMascota, nombre, edad, tipoMascota, "")
                    print(result)
                else:
                    print("Ningún campo ingresado para modificar.")
        else:
            print("Agrege una edad valida")
            

#-------- RECEPCIONISTA ---------

def autenticaRecepcionista():
    run = input("Ingrese su RUT: ")
    password = input("Ingrese su contraseña: ")
    resultado = RecepcionistaDTO().autenticaRecepcionista(run, password)
    return resultado

#-------- OPCIONES Y MENUS -------------
def validaOpc(num):
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc < 1 or opc > num:
                print(f"Debe ingresar una opción entre 1 y {num}.")
            else:
                return opc
        except:
            print("Solo puedes ingresar números. Por favor reintente.")

def menu():
    print("\n=================================")
    print("======= CRUD FICHA MASCOTAS =======")
    print("=================================\n")
    print("1. CRUD Recepcionista")
    print("2. CRUD Clientes")
    print("3. CRUD Mascotas")
    print("4. CRUD Ficha")
    print("5. Salir del Sistema")

def menuCliente():
    print("\n*******************")
    print("*** CRUD Cliente ***")
    print("*******************\n")
    print("1. Ingresar Cliente")
    print("2. Modificar Cliente")
    print("3. Eliminar Cliente")
    print("4. Mostrar todos los Clientes")
    print("5. Volver al Menu Principal")

def menuMascota():
    print("\n*******************")
    print("*** CRUD Mascotas ***")
    print("*******************\n")
    print("1. Ingresar Mascota")
    print("2. Modificar Mascota")
    print("3. Elimina Mascota")
    print("4. Mostrar todas las Mascotas")
    print("5. Volver al Menu Principal")


#---------- INICIALISAR -----------
def inicial():
    cargaInicial()
    while True:
        menu()
        opc = validaOpc(5)
        if opc == 1:
            print("Menu en construcción. Lamentamos las molestias D:")
        elif opc == 2:
            while True:
                menuCliente()
                opc = validaOpc(5)
                if opc == 1:
                    validateAgregarCliente()
                elif opc == 2:
                    validateModificarCliente()
                elif opc == 3:
                    validateEliminarCliente()
                elif opc == 4:
                    validateFindAllClientes()
                else:
                    break    
        elif opc == 3:
            while True:
                    menuMascota()
                    opc = validaOpc(5)
                    if opc == 1:
                        validateAgregarMascota()
                    elif opc == 2:
                        validateModificarMacota()
                    elif opc == 3:
                        validateEliminarMascota()
                    elif opc == 4:
                        validateFindAllMascotas()
                    else:
                        break
        elif opc == 4:
            print("Menu en construccion. Lamentamos las molestias D:")      
        else:
            print("Programa Finalizado.")
            break
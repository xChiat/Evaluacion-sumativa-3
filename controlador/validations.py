from controlador.dto_recep import RecepcionistaDTO
from controlador.dto_cliente import ClienteDTO
from controlador.dto_mascota import MascotaDTO

#Funcion que carga las listas de clase desde la BD
def cargaInicial():
    ClienteDTO().prepareCliente()
    MascotaDTO().prepareMascota()

#Validacion para el ingreso de valores tipo INT
def validaInt(txt):
    while True:
        try:
            opc = int(input(f"Ingresa {txt}: "))
            return opc
        except:
            print("Error de Ingreso, solo puedes ingresar números.")
            
#Validacion para el ingreso de valores tipo STR
def validaStr(txt):
    while True:
        valor = input(f"Ingrese {txt}: ").strip()
        if valor:
            return valor
        else:
            print("Campo incorrecto, no debe estar vacío.")

#Validacion para listar todos los cargos
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

#Validacion para listar todos las comunas
def validateFindAllMascotas():
    print("\n--------------------")
    print("Listado de Mascotas.")
    print("--------------------\n")
    print("")
    result = MascotaDTO().listarMascotas()
    if len(result) > 0:
        for com in result:
            print(com)
    else:
        print("No hay Comunas Registradas.")

#Validación para listar un Cliente.
def validateBuscarCliente(run):
    result = ClienteDTO().buscarCliente(run)
    if result is None:
        return None
    else:
        return result

#Validación para listar una Mascota.
def validateBuscarMascota(idMascota):
    result = MascotaDTO().buscarMascota(idMascota)
    if result is None:
        return None
    else:
        return result 

#Validacion para borrar Clientes
def validateDelCliente():
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
            result = ClienteDTO().delCliente(run)
            return print(result)
        elif confirm == "N":
            return print("Operación Cancelada.")
        else:
            print("Opción invalida, intentalo nuevamente.")
            return validateDelCliente()

#Validacion para borrar Mascotas
def validateDelMascota():
    print("\n--------------------")
    print("Eliminar Mascota.")
    print("--------------------\n")
    idMascota = validaInt("Comuna")
    val = validateBuscarMascota(idMascota)
    if val is None:
        return print("La Mascota no existe, no se puede Eliminar.")
    else:
        print("¿Estas seguro que deseas eliminar a la Mascota?")
        confirm = input("Presiona Y/y para Confirmar o N/n para Cancelar:")
        confirm = confirm.upper()
        if confirm == "Y":
            result = MascotaDTO().delMascota(idMascota)
            return print(result)
        elif confirm == "N":
            return print("Operación Cancelada.")
        else:
            print("Opción invalida, intentalo nuevamente.")
            return validateDelMascota()

#Validacion para agregar Cargos
def validateAddCliente():
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
    # Asegura que los campos no estén vacíos
        if not nombre or not apellido or not correo or not telefono:
            return print("Todos los campos son requeridos. Operación Cancelada.")
        else:
            result = ClienteDTO().addCliente(run, nombre, apellido, telefono, correo)
            print(result)

#Validacion para agregar Comunas
def validateAddMascota():
    print("\n--------------------")
    print("Agregar Mascota.")
    print("--------------------\n")
    # Pedir ID del cliente existente
    run = validaStr("RUT del Cliente")
    cliente_existente = validateBuscarCliente(run)

    if cliente_existente is None:
        return print("El Cliente no existe. Operación Cancelada.")
    else:
        # Pedir detalles de la mascota
        idMascota = validaInt("el id de la mascota")
        val = validateBuscarMascota(idMascota)
        if val is not None:
            return print("La mascota ya existe, no puedes volver a agregarla")
        else:
            nombre = validaStr("el Nombre de la Mascota")
            edad = validaInt("Edad de la Mascota")
            tipo = validaStr("Tipo de Mascota (Perro o Gato)")
        # Asegura que los campos no estén vacíos
            if not nombre or not edad or not tipo:
                return print("Todos los campos son requeridos. Operación Cancelada.")

        # Agregar la mascota al cliente existente
            result = MascotaDTO().addMascota(idMascota, nombre, edad, tipo, run)
            print(result)

#Validacion para modificar Cargos
def validateUpdateCliente():
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

        # Validar y realizar la actualización
        if nombre or apellido or telefono or correo:
            result = ClienteDTO().updateCliente(run, nombre, apellido, telefono, correo)
            print(result)
        else:
            print("Ningún campo ingresado para modificar.")
            
def validateUpdateMascota():
    print("\n--------------------")
    print("Modificar Mascota.")
    print("--------------------\n")
    idMascota = validaInt("el id de la mascota")
    val = validateBuscarMascota(idMascota)
    if val is None:
        return print("La Mascota no existe, no puedes modificarla.")
    else:
        #rellenar despues
        pass

#validador de contraseña de ADM
def validarLogin():
    run = input("Ingrese su RUT: ")
    password = input("Ingrese su contraseña: ")
    resultado = RecepcionistaDTO().validarLogin(run, password)
    return resultado

#validador de opciones para los menus
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

#Menu Principal
def menu():
    print("\n=================================")
    print("======= CRUD FICHA MASCOTAS =======")
    print("=================================\n")
    print("1. CRUD Recepcionista")
    print("2. CRUD Clientes")
    print("3. CRUD Mascotas")
    print("4. CRUD Ficha")
    print("5. Salir del Sistema")

#Menu de Cargos
def menuCargo():
    print("\n*******************")
    print("*** CRUD Cliente ***")
    print("*******************\n")
    print("1. Ingresar Cliente")
    print("2. Modificar Cliente")
    print("3. Eliminar Cliente")
    print("4. Mostrar todos los Clientes")
    print("5. Volver al Menu Principal")

#Menu de comunas
def menuComuna():
    print("\n*******************")
    print("*** CRUD Mascotas ***")
    print("*******************\n")
    print("1. Ingresar Mascota")
    print("2. Modificar Mascota")
    print("3. Elimina Mascota")
    print("4. Mostrar todas las Mascotas")
    print("5. Volver al Menu Principal")


#Loops de los menus
def inicial():
    cargaInicial()
    while True:
        menu()
        opc = validaOpc(5)
        if opc == 1:
            print("Menu en construcción. Lamentamos las molestias D:")
        elif opc == 2:
            while True:
                menuCargo()
                opc = validaOpc(5)
                if opc == 1:
                    validateAddCliente()
                elif opc == 2:
                    validateUpdateCliente()
                elif opc == 3:
                    validateDelCliente()
                elif opc == 4:
                    validateFindAllClientes()
                else:
                    break    
        elif opc == 3:
            while True:
                    menuComuna()
                    opc = validaOpc(5)
                    if opc == 1:
                        validateAddMascota()
                    elif opc == 2:
                        #validateFindComuna()
                        validateUpdateMascota()
                    elif opc == 3:
                        validateDelMascota()
                    elif opc == 4:
                        validateFindAllMascotas()
                    else:
                        break
        elif opc == 4:
            print("Menu en construccion. Lamentamos las molestias D:")      
        else:
            print("Programa Finalizado.")
            break
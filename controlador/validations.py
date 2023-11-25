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
            opc = int(input(f"Ingresa el codigo de {txt}: "))
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
        for car in result:
            print(car)
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
    if val:
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
    idMascota = validaInt("Comuna")
    val = validateBuscarMascota(idMascota)
    if val:
        return print("El Codigo de Comuna ya existe, no puedes volver a registrarlo.")
    else:
        nombre = validaStr("Nombre del Cliente")
        edad = validaInt("Apellido del Cliente")
        tipo = validaStr("Correo del Cliente")
        cliente = validaStr("RUT Cliente")
    # Asegura que los campos no estén vacíos
        if not nombre or not edad or not tipo or not cliente:
            return print("Todos los campos son requeridos. Operación Cancelada.")
        else:
            result = ClienteDTO().addCliente(idMascota, nombre, edad, tipo, cliente)
            print(result)

#Validacion para modificar Cargos
def validateUpdateCargo():
    print("\n--------------------")
    print("Modificar Cargo.")
    print("--------------------\n")
    idCargo = validaInt("Cargo")
    val = validateFindCargo(idCargo)
    if val is None:
        return print("El Cargo no existe, no puedes modificarlo.")
    else:
        descCar = input("Ingrese Nueva Descripcion del cargo o Presione ENTER para cancelar: ")
        if len(descCar) == 0:
            return print("Operación Cancelada.")
        elif len(descCar) < 3:
            print("Campo incorrecto, debes ingresar al menos 3 valores.")
            return validateUpdateCargo()
        else:
            print(CargoDTO().updateCargo(idCargo, descCar))

def validateUpdateComuna():
    print("\n--------------------")
    print("Modificar Comuna.")
    print("--------------------\n")
    idComuna = validaInt("Comuna")
    val = validateFindComuna(idComuna)
    if val is None:
        return print("La Comuna no existe, no puedes modificarla.")
    else:
        descCom = input("Ingrese Nueva Descripcion de la Comuna o Presione ENTER para cancelar: ")
        if len(descCom) == 0:
            return print("Operación Cancelada.")
        elif len(descCom) < 3:
            print("Campo incorrecto, debes ingresar al menos 3 valores.")
            return validateUpdateComuna()
        else:
            print(ComunaDTO().updateComuna(idComuna, descCom))

#validador de contraseña de ADM
def validarLogin():
    mail = input("Ingrese correo (xxxx@xxxx): ")
    password = input("Ingrese contraseña: ")
    resultado = EmpleadoDTO().validarLogin(mail, password)
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
        opc = validaOpc(4)
        if opc == 1:
            print("Menu en construcción. Lamentamos las molestias.")
        elif opc == 2:
            while True:
                menuCargo()
                opc = validaOpc(5)
                if opc == 1:
                    validateAddCargo()
                elif opc == 2:
                    validateUpdateCargo()
                elif opc == 3:
                    validateDelCargo()
                elif opc == 4:
                    validateFindAllCargos()
                else:
                    break    
        elif opc == 3:
            while True:
                    menuComuna()
                    opc = validaOpc(5)
                    if opc == 1:
                        validateAddComuna()
                    elif opc == 2:
                        #validateFindComuna()
                        validateUpdateComuna()
                    elif opc == 3:
                        validateDelComuna()
                    elif opc == 4:
                        validateFindAllComunas()
                    else:
                        break  
        else:
            print("Programa Finalizado.")
            break
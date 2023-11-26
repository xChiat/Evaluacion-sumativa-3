from controlador.validations import inicial, validarLogin


# login
intentos = 1
print("\n=== Minimarket Fenix ===\n")
while intentos <= 3:
    try:
        result = validarLogin()
        #result = 1
        if result is not None:
            print("-Acceso Permitido-")
            inicial()
            break
        else:
            print("-Usuario o Contraseña incorrecta-")
            intentos += 1
    except Exception as ex:
        print(ex)
        print("-Intente nuevamente-")
if intentos == 4:
    print("-Contraseña bloqueada-")
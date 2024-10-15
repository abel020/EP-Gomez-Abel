
def PedirContraseña(medidor):
    Usuario = input("Usuario: ")
    Contraseña = input("Contraseña: ")
    
    GetUsuario = open("login.txt", 'rt', encoding='utf-8')
    GetUsuario1 = GetUsuario.read().splitlines()
    GetContraseña = open("clave.txt", 'rt', encoding='utf-8')
    GetContraseña2 = GetContraseña.read().splitlines()
    
    if Usuario in GetUsuario1 and Contraseña in GetContraseña2:
        print("Bienvenido!")
        menu()
    else:
        print("Usuario o contraseña incorrectos")
        if medidor == False:
            exit()
        PedirContraseña(False)
    
def lista_Personas():
    GetPersonasDni = open("dni.txt", 'rt', encoding='utf-8')
    PersonasDni = GetPersonasDni.read().splitlines()

    GetPersonasNombre = open("nombres.txt", 'rt', encoding='utf-8')
    PersonasNombre = GetPersonasNombre.read().splitlines()

    GetPersonasApellido = open("apellidos.txt", 'rt', encoding='utf-8')
    PersonasApellido = GetPersonasApellido.read().splitlines()
    
    print("DNI       Nombre       Apellido")
    print("-------------------------------")

    for i in range(len(PersonasDni)):
        print(f"{PersonasDni[i]}   {PersonasNombre[i]}   {PersonasApellido[i]}")


def Agregar_Personas():
    Dni = input("Dni: ")
    Nombres = input("Nombres: ")
    Apellidos = input("Apellidos: ")
    archivo1 = open("dni.txt","at")
    archivo2 = open("nombres.txt","at")
    archivo3 = open("apellidos.txt","at")
    archivo1.write("\n"+Dni)
    archivo2.write("\n"+Nombres)
    archivo3.write("\n"+Apellidos)
    archivo1.close()
    archivo2.close()
    archivo3.close()
    print("Persona Agregada correctamente...")

def menu():
    print("Datos persona")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")
    try:
        opcion = int(input("\nDigite la opción deseada: "))
        if opcion == 1:
            lista_Personas()
            menu()
        elif opcion == 2:
            Agregar_Personas()
            menu()
        elif opcion == 3:
            exit()    
    except ValueError:
        print("Debe ingresar un número")

PedirContraseña(True)


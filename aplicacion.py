
def PedirContraseña(medidor):
    Usuario = input("Usuario: ")
    Contraseña = input("Contraseña: ")
    
    GetUsuario = open("login.txt", 'rt', encoding='utf-8')
    GetUsuario1 = GetUsuario.read()
    GetContraseña = open("clave.txt", 'rt', encoding='utf-8')
    GetContraseña2 = GetContraseña.read()
    
    if Usuario in GetUsuario1 and Contraseña in GetContraseña2:
        print("Bienvenido!")
        menu()
    else:
        print("Usuario o contraseña incorrectos")
        if medidor == False:
            exit()
        PedirContraseña(False)
    
def lista_Personas():
    print("l")
def Agregar_Personas():
    print("a")

def menu():
    print("Datos persona")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")
    try:
        opcion = int(input("\nDigite la opción deseada: "))
        if opcion == 1:
            lista_Personas
            menu()
        elif opcion == 2:
            Agregar_Personas()
            menu()
        elif opcion == 3:
            exit()    
    except ValueError:
        print("Debe ingresar un número")

PedirContraseña(True)
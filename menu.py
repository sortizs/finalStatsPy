import file
import login
import signup
import json

from user import User

print('¡¡¡BIENVENIDO!!!')
print('1. Registrarse')
print('2. Iniciar sesión')

CURRENT_USER: User

def menu() -> None:
    """Presenta las opciones de menu al usuario
    """
    opt = int(input('Elija una opción(1-2): '))
    if opt == 1:
        username = input('Ingrese el nombre de usuario: ')
        password = input('Ingrese la contraseña: ')
        CURRENT_USER = User(username, password)
        signup.validUser(CURRENT_USER)
        login.login(CURRENT_USER)
    elif opt == 2:
        username = input('Nombre de usuario: ')
        password = input('Contraseña: ')
        CURRENT_USER = User(username, password)
        if login.login(CURRENT_USER):
            print(json.dumps(file.getUserData(CURRENT_USER.username)['amigos'], sort_keys=True, indent=4))
    else:
        print('Opcion incorrecta.')

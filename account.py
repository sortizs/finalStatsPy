# Account related functions
import re
import json
import data.file as f
from user import User

CURRENT_USER: User = None

def saveNewUser(user: User) -> None:
    """Alamacena el usuario en el archivo users.txt

    Args:
        user (User): Usuario con nombre y contraseña
    """
    with open('users.txt', 'a') as f:
        f.write(user.username + ';' + user.password + '\n')
        f.close()
        print('Usuario creado con exito.')

def validateUser(user: User) -> None:
    """Valida los datos del usuario ingresado

    Args:
        user (User): Usuario con nombre y contraseña
    """
    names = []
    if re.fullmatch(r"[A-Za-z]+", user.username):
        names = f.getNames()
        if user.username in names:
            print('El usuario ya existe.')
        else:
            repeatPassword = input('Ingrese la contraseña de nuevo: ')
            if repeatPassword == user.password:
                saveNewUser(user)
            else:
                print('La contraseña debe ser igual.')
    else:
        print('El nombre de usuario no admite caracteres especiales ni números.')

def signup():
    username = input('Ingrese el nombre de usuario: ')
    password = input('Ingrese la contraseña: ')
    CURRENT_USER = User(username, password)
    validateUser(CURRENT_USER)

def login() -> None:
    """Realiza las validaciones correspondientes para el inicio de sesión

    Args:
        user (User): Usuario con nombre y contraseña
    """
    
    attempt = 2
    username = input('Nombre de usuario: ')
    password = input('Contraseña: ')
    CURRENT_USER = User(username, password)
    user = f.getUser(CURRENT_USER.username)

    if user:
        for attempt in range(attempt, 0, -1):
            if(user.password == CURRENT_USER.password):
                print(f'{len(User.friends(CURRENT_USER.username))} amigos')
                print(f'{User.friendRequests()} solicitudes de amistad')
                print(f'Tiene {len(User.getMessages(CURRENT_USER.username))} mensajes')
            else:
                print('Contraseña incorrecta.')
                CURRENT_USER.password = input('Ingrese de nuevo la contraseña: ')
        else:
            print('Ha bloqueado su cuenta')
            # f.setUserData(user.username, 'estado', 'bloqueado')

def deleteAccount() -> None:
    password = input('Confirme la contraseña para eliminar su cuenta: ')
    if password == CURRENT_USER.password:
        f.deleteUser(CURRENT_USER.username)
    else:
        print('Contraseña incorrecta')
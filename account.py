# Account related functions
import re
import data.file as f
from datetime import datetime
from user import User

def saveNewUser(user: User) -> None:
    """Crea el usuario en el archivo users.txt

    Args:
        user (User): Usuario con nombre de usuario y contraseña
    """
    with open('users.txt', 'a') as f:
        f.write(user.username + ';' + user.password + '\n')
        f.close()
        print('Usuario creado con exito.')

def validateUser(user: User) -> None:
    """Valida los datos del usuario ingresado

    Args:
        user (User): Usuario con nombre de usuario y contraseña
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

def signup() -> None:
    username = input('Ingrese el nombre de usuario: ')
    password = input('Ingrese la contraseña: ')
    currentUser = User(username, password)
    validateUser(currentUser)

def login() -> User:
    """Realiza las validaciones correspondientes para el inicio de sesión

    Args:
        user (User): Usuario con nombre de usuario y contraseña
    """
    attempt = 2
    username = input('Nombre de usuario: ')
    password = input('Contraseña: ')
    currentUser = User(username, password)
    user = f.getUser(currentUser.username)
    userData = f.getUserData(currentUser.username)

    if user:
        if userData['estado'] == 'activo':
            for attempt in range(attempt, 0, -1):
                if(user[1] == currentUser.password):
                    print(f'{len(User.friends(currentUser.username))} amigos')
                    # print(f'{User.friendRequests()} solicitudes de amistad')
                    print(f'Tiene {len(User.getMessages(currentUser.username))} mensajes')
                    return(currentUser)
                else:
                    print('Contraseña incorrecta.')
                    currentUser.password = input('Ingrese de nuevo la contraseña: ')
            else:
                print('Ha bloqueado su cuenta')
                f.setUserData(user[0], 'estado', 'bloqueado')
                return None
        else:
            print(f'El usuario {currentUser.username} se encuentra inactivo.')
    else:
        print('El usuario no se encuentra registrado')
        return None

def deleteAccount(user: User) -> None:
    """Desactiva la cuenta tras verificar la contraseña
    """
    password = input('Confirme la contraseña para eliminar su cuenta: ')
    if password == user.password:
        f.setUserData(user.username, 'estado', 'inactivo')
        f.setUserData(user.username, 'fechaRetiro', datetime.today().strftime('%d/%m/%Y'))
    else:
        print('Contraseña incorrecta')
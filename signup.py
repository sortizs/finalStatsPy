import re
import file
from user import User
    
def saveNewUser(user: User):
    with open('users.txt', 'a') as f:
        f.write(user.username + ';' + user.password + '\n')
        f.close()
        print('Usuario creado con exito.')

def validUser(user: User):
    names = []
    if re.fullmatch(r"[A-Za-z]+", user.username):
        names = file.getNames()
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
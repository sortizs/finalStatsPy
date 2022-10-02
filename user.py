import re
from file import getNames

class User:

    name: str
    password: str

    def __init__(self, name: str, password) -> None:
        self.name = name.lower()
        self.password = password

    def saveNewUser(self):
        with open('users.txt', 'a') as f:
            f.write(self.name + ';' + self.password + '\n')
            f.close()
            print('Usuario creado con exito.')

    def validUser(self) -> bool:
        names = []
        if re.fullmatch(r"[A-Za-z]+", self.name):
            names = getNames()
            if self.name in names:
                print('El usuario ya existe.')
            else:
                repeatPassword = input('Ingrese la contraseña de nuevo: ')
                if repeatPassword == self.password:
                    self.saveNewUser()
                else:
                    print('La contraseña debe ser igual.')
        else:
            print('El nombre de usuario no admite caracteres especiales ni números.')

    def completeProfile():
        pass
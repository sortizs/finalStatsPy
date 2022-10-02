from mimetypes import init

class User:

    name: str
    password: str

    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password

    def saveNewUser(self):
        with open('users.txt', 'a') as f:
            f.write(self.name + ';' + self.password + '\n')
            f.close()
            print('Usuario creado con exito.')

    def validateUser(self):
        """ with open('users.txt', 'r') as file:
            fileLines = file.read().split('\n')
            print(fileLines) """
        repeatPassword = input('Ingrese la contraseña de nuevo: ')
        if repeatPassword == self.password:
            return True
        else:
            return False

    def completeProfile():
        pass
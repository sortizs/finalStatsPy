from user import User

username = input('Ingrese el nombre de usuario: ')
password = input('Ingrese la contraseña: ')

newUser = User(username, password)
newUser.validUser()

from user import User;

username = input('Ingrese el nombre de usuario: ')
password = input('Ingrese la contraseña: ')

newUser = User(username, password)
if newUser.validateUser():
    newUser.saveNewUser()
else:
    print('La contraseña debe ser igual')

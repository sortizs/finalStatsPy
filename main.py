
import menu
import data.file as f
import account as acc
from user import User as user

menuOpt = menu.startMenu()

if menuOpt == 1:
    # Registrar cuenta
    acc.signup()
elif menuOpt == 2:
    # Iniciar sesion
    acc.login()
    loggedMenuOpt = menu.loggedMenu()
    while acc.CURRENT_USER:
        if loggedMenuOpt == 1:
            # Ver usuarios registrados
            for name in f.getNames():
                print(name)
        elif loggedMenuOpt == 2:
            # Enviar solicitud de amistad
            pass
        elif loggedMenuOpt == 3:
            # Ver solicitudes de amistad pendientes
            user.friendRequests()
        elif loggedMenuOpt == 4:
            # Ver mensajes
            for message in user.getMessages(acc.CURRENT_USER.username):
                print(message)
        elif loggedMenuOpt == 5:
            # Enviar mensaje
            receiver = input('Destinatario: ')
            message = input('Mensaje: ')
            user.sendMessage(acc.CURRENT_USER.username, receiver, message)
        elif loggedMenuOpt == 6:
            # Usuarios con intereses similares
            pass
        elif loggedMenuOpt == 7:
            # Completar perfil
            pass
        elif loggedMenuOpt == 8:
            # Darse de baja
            acc.deleteAccount()
        elif loggedMenuOpt == 9:
            # Cerrar sesión
            acc.CURRENT_USER = None
        else:
            print('Opción incorrecta.')
elif menuOpt == 3:
    # Estadísticas
    pass
elif menuOpt == 4:
    # Terminar aplicación
    acc.CURRENT_USER = None
else:
    print('Opcion incorrecta.')

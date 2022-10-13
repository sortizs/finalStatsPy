
import menu
import data.file as f
import account as acc
from user import User as user

menuOpt = menu.startMenu()

if menuOpt == 1:
    acc.signup()
elif menuOpt == 2:
    acc.login()
    loggedMenuOpt = menu.loggedMenu()
    while acc.CURRENT_USER:
        if loggedMenuOpt == 1:
            # Ver usuarios registrados
            print(f.getNames())
        elif loggedMenuOpt == 2:
            # Enviar solicitud de amistad
            pass
        elif loggedMenuOpt == 3:
            # Ver solicitudes de amistad pendientes
            user.friendRequests()
        elif loggedMenuOpt == 4:
            # Ver mensajes
            print(user.getMessages(acc.CURRENT_USER.username))
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
    pass
elif menuOpt == 4:
    acc.CURRENT_USER = None
else:
    print('Opcion incorrecta.')

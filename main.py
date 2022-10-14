
import menu
import data.file as f
import account as acc
from user import User as user

while True:
    menuOpt = menu.startMenu()
    if menuOpt == 1:
        # Registrar cuenta
        acc.signup()
    elif menuOpt == 2:
        # Iniciar sesion
        loggedUser = acc.login()
        while loggedUser:
            loggedMenuOpt = menu.loggedMenu()
            if loggedMenuOpt == 1:
                # Ver usuarios registrados
                for name in f.getNames():
                    print(name)
            elif loggedMenuOpt == 2:
                # Enviar solicitud de amistad
                pass
            elif loggedMenuOpt == 3:
                # Ver solicitudes de amistad pendientes
                pass
            elif loggedMenuOpt == 4:
                # Ver mensajes
                for message in user.getMessages(loggedUser.username):
                    print(message)
            elif loggedMenuOpt == 5:
                # Enviar mensaje
                receiver = input('Destinatario: ')
                message = input('Mensaje: ')
                user.sendMessage(loggedUser.username, receiver, message)
            elif loggedMenuOpt == 6:
                # Usuarios con gustos similares
                similarHobbies = user.similarHobbies(loggedUser.username)
                print('\nUsuarios con gustos similares:')
                for similarHobbie in similarHobbies:
                    print(f"- {similarHobbie}")
                pass
            elif loggedMenuOpt == 7:
                # Completar perfil
                user.completeProfile(loggedUser.username)
                pass
            elif loggedMenuOpt == 8:
                # Darse de baja
                acc.deleteAccount(loggedUser)
            elif loggedMenuOpt == 9:
                # Cerrar sesión
                loggedUser = None
            else:
                print('Opción incorrecta.')
    elif menuOpt == 3:
        statsOpt = menu.statisticsMenu()
        if statsOpt == 1:
            pass
        elif statsOpt == 2:
            pass
        elif statsOpt == 3:
            pass
        elif statsOpt == 4:
            pass
        else:
            print('Opción incorrecta.')
    elif menuOpt == 4:
        # Terminar aplicación
        break
    else:
        print('Opcion incorrecta.')


import file
from user import User

def login(user: User) -> bool:
    """Realiza las validaciones correspondientes para el inicio de sesión

    Args:
        user (User): Usuario con nombre y contraseña

    Returns:
        bool: Estado exitoso de la operación de inicio de sesión
    """
    attempt = 2

    _user = file.getUser(user.username)

    if _user:
        for attempt in range(attempt, 0, -1):
            if(user.password == _user.password):
                return True
            else:
                print('Contraseña incorrecta.')
                user.password = input('Ingrese la contraseña de nuevo: ')
        else:
            print('Ha bloqueado su cuenta')
            file.setUserData(user.username, 'estado', 'bloqueado')
            return False
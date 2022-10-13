#!

print('¡¡¡BIENVENIDO!!!')

def startMenu() -> int:
    """Muestra el menu principal de la aplicación

    Returns:
        int: Retorna la opción elegida por el usuario
    """
    print('1. Registrarse')
    print('2. Iniciar sesión')
    print('3. Estadísticas de la aplicación')
    print('4. Cerrar aplicación')
    opt = int(input('Elija una opción(1-4): '))
    return opt

def loggedMenu() -> int:
    """Muestra el menú de inicio de sesión

    Returns:
        int: Retorna la opción elegida por el usuario
    """
    print('\n1. Ver usuarios registrados')
    print('2. Enviar solicitud de amistad')
    print('3. Ver solicitudes de amistad pendientes')
    print('4. Ver mensajes')
    print('5. Enviar mensaje')
    print('6. Usuarios con intereses similares')
    print('7. Completar perfil')
    print('8. Darse de baja')
    print('9. Cerrar sesión')
    opt = int(input('Elija una opción(1-9): '))
    return opt
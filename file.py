import json
from typing import List
from user import User


def getNames() -> List[str]:
    """Obtiene la lista de nombres del archivo txt

    Returns:
        List[str]: Lista de nombres registrados
    """
    names = []
    with open('users.txt', 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            for line in line.split(';'):
                names.append(line)
        f.close()
    del names[1::2]
    return names


def getUser(username: str) -> User:
    """Obtiene el usuario y la contraseña desde el archivo user.txt

    Args:
        username (str): Nombre de usuario

    Returns:
        User: Nombre de usuario y contraseña desde el archivo user.txt
    """
    indexOf: int
    names = getNames()
    if username in names:
        indexOf = names.index(username)
        with open('users.txt', 'r') as f:
            lines = f.read().split('\n')
            line = lines[indexOf].split(';')
            f.close()
            return User(line[0], line[1])
    else:
        return None


def getUserData(username: str) -> dict:
    """Obtiene la información del usuario desde el archivo userData.json

    Args:
        username (str): Nombre de usuario

    Returns:
        dict: Devuelve un diccionario con la información del usuario
    """
    with open('userData.json', 'r') as f:
        data = json.load(f)
        f.close
    return data[username]


def setUserData(username: str, param: str, value: str) -> None:
    """Edita la información del usuario en el archivo userData.json

    Args:
        username (str): Nombre de usuario
        param (str): Parametro a modificar
        value (str): Valor del parametro a modificar
    """
    with open('userData.json', 'r+') as f:
        data = json.load(f)
        data[username][param] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
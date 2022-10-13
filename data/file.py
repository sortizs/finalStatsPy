import json
from datetime import date, datetime
from operator import indexOf
from typing import List, Tuple

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


def getUser(username: str) -> Tuple[str, str]:
    """btiene el usuario y la contraseña desde el archivo user.txt

    Args:
        username (str): Nombre de usuario

    Returns:
        Tuple[str, str]: Nombre de usuario, contraseña
    """
    indexOf: int
    names = getNames()
    if username in names:
        indexOf = names.index(username)
        with open('users.txt', 'r') as f:
            lines = f.read().split('\n')
            line = lines[indexOf].split(';')
            f.close()
            return line[0], line[1]
    else:
        return None

def deleteUser(username: str):
    indexOf: int
    names = getNames()
    if username in names:
        indexOf = names.index(username)
        with open('users.txt', 'r+') as f:
            lines = f.read().split('\n')
            lines.pop(indexOf)
            f.seek(0)
            f.write('\n'.join(lines))
            f.truncate()
            f.close()


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

def getUserMessages(username: str) -> List[str]:
    """Obtiene la lista de mensajes que le han enviado al usuario

    Args:
        username (str): Nombre de usuario

    Returns:
        List[str]: Lista de mensajes
    """
    with open(f'../mensajes/{username}.txt', 'r') as f:
        messages: List[str] = f.read().split('\n')
    return messages

def saveMessage(username:str, receiver:str, message: str):
    date = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    with open(f'../messages/{receiver}.txt', 'a') as f:
        f.write(f'El {date} {username} escribió: {message}\n')
        f.close()
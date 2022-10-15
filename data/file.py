import json
from datetime import datetime
from operator import indexOf
from typing import List, Tuple

def getNames() -> List[str]:
    """Obtiene la lista de nombres del archivo txt

    Returns:
        List[str]: Lista de nombres registrados
    """
    names = []
    with open('data/users.txt', 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            for line in line.split(';'):
                names.append(line)
        f.close()
    del names[1::2]
    return names


def getUser(username: str) -> Tuple[str, str]:
    """Obtiene el usuario y la contraseña desde el archivo users.txt

    Args:
        username (str): Nombre de usuario

    Returns:
        Tuple[str, str]: Nombre de usuario, contraseña
    """
    indexOf: int
    names = getNames()
    if username in names:
        indexOf = names.index(username)
        with open('data/users.txt', 'r') as f:
            lines = f.read().split('\n')
            line = lines[indexOf].split(';')
            f.close()
            return line[0], line[1]
    else:
        return None

def deleteUser(username: str) -> None:
    """Elimina el usuario y la contraseña del archivo users.txt

    Args:
        username (str): Nombre del usuario a eliminar
    """
    indexOf: int
    names = getNames()
    if username in names:
        indexOf = names.index(username)
        with open('data/users.txt', 'r+') as f:
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
    with open('data/userData.json', 'r') as f:
        data = json.load(f)
        f.close()
    if username in data:
        return data[username]
    else:
        return {}
    
def setUserData(username: str, param: str, value: str) -> None:
    """Edita la información del usuario en el archivo userData.json

    Args:
        username (str): Nombre de usuario
        param (str): Parametro a modificar
        value (str): Valor del parametro a modificar
    """
    with open('data/userData.json', 'r+') as f:
        data = json.load(f)
        data[username][param] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def getUserMessages(username: str) -> List[str]:
    """Obtiene la lista de mensajes desde la carpeta mensajes por usuario

    Args:
        username (str): Nombre de usuario

    Returns:
        List[str]: Lista de mensajes recibidos
    """
    with open(f'mensajes/{username}.txt', 'a+') as f:
        messages: List[str] = f.read().split('\n')
    return messages

def saveMessage(username:str, receiver:str, message: str):
    """Guarda el mensaje en la carpeta Mensajes, en el archivo correspondiente

    Args:
        username (str): Nombre del usuario que envía el mensaje
        receiver (str): Nombre del usuario que recibe el mensaje
        message (str): Mensaje
    """
    date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open(f'./mensajes/{receiver}.txt', 'a') as f:
        f.write(f'El {date} {username} escribió: {message}\n')
        f.close()

def saveProfile(username: str, profile: dict) -> None:
    """Actualiza la información del perfil en userData.json

    Args:
        username (str): Nombre del usuario a actualizar
        profile (dict): Perfil con la información a actualizar
    """
    userData = getUserData(username)

    userData['nombre'] = profile['nombre']
    userData['apellido'] = profile['apellido']
    userData['edad'] = profile['edad']
    userData['gustos'] = profile['gustos']
    userData['genero'] = profile['genero']

    if 'fechaIngreso' not in userData:
        userData['fechaIngreso'] = datetime.today().strftime('%d/%m/%Y')

    if 'fechaBloqueo' not in userData:
        userData['fechaBloqueo'] = None

    if 'fechaRetiro' not in userData:
        userData['fechaRetiro'] = None

    if 'estado' not in userData:
        userData['estado'] = 'activo'

    with open('./data/userData.json', 'r+') as f:
        data = json.load(f)
        data[username] = userData
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()
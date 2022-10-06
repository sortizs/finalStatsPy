
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

def getUser(username) -> User:
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

def getUserData(username):
    with open('userData.json', 'r') as f:
        data = json.load(f)
        f.close
    return data[username]

def setUserData(username, param, value):
    with open('userData.json', 'r+') as f:
        data = json.load(f)
        data[username][param] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

import json
import data.file as f
from typing import List

class User:

    username: str
    password: str

    def __init__(self, username: str, password: str) -> None:
        """Constructor de la clase usuario

        Args:
            username (str): Nombre de usuario
            password (str): Contraseña
        """
        self.username = username.lower()
        self.password = password

    def friends(username: str)  -> List[str]:
        userData = f.getUserData(username)
        return userData['amigos']

    def friendRequests():
        pass

    def getMessages(username: str) -> List[str]:
        messages = f.getUserMessages(username)
        return messages

    def sendMessage(username: str, receiver: str, message: str):
        if receiver in f.getNames():
            f.saveMessage(username, receiver, message)
        else:
            print('El usuario al que quiere enviar el mensaje no está registrado')

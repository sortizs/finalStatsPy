
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
        """Obtiene la lista de amigos por nombre de usuario

        Args:
            username (str): Nombre de usuario

        Returns:
            List[str]: Lista de amigos
        """
        userData = f.getUserData(username)
        return userData['amigos']

    def friendRequests():
        pass

    def getMessages(username: str) -> List[str]:
        """Obtiene los mensajes que el usuario ha recibido

        Args:
            username (str): Nombre de usuario

        Returns:
            List[str]: Lista de mensajes recibidos
        """
        messages = f.getUserMessages(username)
        return messages

    def sendMessage(username: str, receiver: str, message: str) -> None:
        """Envia el mensaje al destinatario

        Args:
            username (str): Nombre del usuario que envia el mensaje
            receiver (str): Nombre del usuario que recibe el mensaje
            message (str): Mensaje
        """
        if receiver in f.getNames():
            f.saveMessage(username, receiver, message)
        else:
            print('El usuario al que quiere enviar el mensaje no se encuentra registrado.')


import re
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
        if 'amigos' in userData:
            return userData['amigos']
        else:
            return []

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

    def completeProfile(username: str) -> None:
        name = input('Nombre: ')
        lastname = input('Apellido: ')
        age = int(input('Edad: '))
        hobbies = input('Gustos (separados por coma): ').split(', ')
        gender = input('Genero (M-F): ')
        _hobbies = []
        for hobbie in hobbies:
            _hobbies.append(re.sub(r'^\s+|\s+$', '', hobbie))

        profile = {
            'nombre': name,
            'apellido': lastname,
            'edad': age,
            'gustos': _hobbies,
            'genero': gender
        }
        f.saveProfile(username, profile)

    def similarHobbies(username: str) -> List[str]:
        similarUsers = []
        users = f.getNames()
        users.remove(username)
        myHobbies = f.getUserData(username)['gustos']
        for user in users:
            if 'gustos' in f.getUserData(user):
                hobbies = f.getUserData(user)['gustos']
                for myHobbie in myHobbies:
                    if myHobbie in hobbies:
                        similarUsers.append(user)
        return list(dict.fromkeys(similarUsers))

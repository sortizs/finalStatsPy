
import json

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

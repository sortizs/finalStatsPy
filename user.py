
import json

class User:

    username: str
    password: str

    def __init__(self, username: str, password) -> None:
        self.username = username.lower()
        self.password = password

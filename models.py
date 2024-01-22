from dataclasses import dataclass

@dataclass
class User:
    email: str
    password : str

    def __init__(self, email, password):
        self.email = email
        self.password = password
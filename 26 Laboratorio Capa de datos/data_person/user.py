

class User:
    def __init__(self, id_user=None, username=None, password=None) -> None:
        self._id_user = id_user
        self._username = username
        self._password = password

    def __str__(self) -> str:
        return f'Usuario: {self._id_user} \nNombre: {self._username} \nContraseña: {self._password}'

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        encrypted_pass = encrypt_pass(password)
        self._password = encrypted_pass


def encrypt_pass(password):
    pass


if __name__ == "__main__":
    user = User(1, 'pedrovazquezg', 'HolaMundo')

    print(user)

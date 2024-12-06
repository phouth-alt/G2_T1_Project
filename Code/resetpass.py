import hashlib
class ResetPass:
    def __init__(self, username,password):
        self.username = username
        self.__password = password
    def encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    def resetpass(self):
        with open("data.txt", 'r') as file:
            pass
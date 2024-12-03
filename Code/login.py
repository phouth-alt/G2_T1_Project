import hashlib
class Login:
    def __init__(self,username, password):
        self.username = username
        self.__password = self.encrypt_password(password)
    def encrypt_password(self, password):
        self.encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        return self.encrypted_password
    def check_password(self):
        with open("data.txt", "r") as file:
            if self.encrypt_password == file.readlines():
                return True
            else:
                return False
            
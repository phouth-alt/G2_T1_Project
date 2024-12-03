import re
import hashlib
class Register:
    def __init__(self,username, password, phone):
        self.username = username
        self.__password = self.encrypt_password(password)
        self.__phone = phone
    def encrypt_password(self, password):
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        return encrypted_password
    def pass_strength(self, password):
        flag = 0
        while True:
            if(len(self.__password) <= 8):
                flag = -1
                break
            elif not re.search("[a-z]", self.__password):
                flag = -1
                break
            elif not re.search("[A-Z]", self.__password):
                flag = -1
                break
            elif not re.search("[0-9]", self.__password):
                flag = -1
                break
            elif not re.search("[!@#$%^&*()]", self.__password):
                flag = -1
                break
            elif re.search("\s", self.__password):
                flag = -1
                break
            else:
                flag = 0
                print("Valid Password")
                break
            
        if flag == -1: 
            print("Not a Valid Password")
    def display_details(self):
        print(f"Username: {self.username}")
        print(f"Phone: {self.__phone}")
        print(f"Encrypted Password: {self.__password}")
password = "R@m@_f0rtu9e$"
user1 = Register("phanphouth",password ,85976899776)
user1.pass_strength(password)
user1.display_details()
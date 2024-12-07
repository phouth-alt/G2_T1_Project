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
    def check_user(self):
        with open("data.txt", 'r') as file:
            read_data = file.readlines()
            if read_data == self.__phone:
                return True
            else:
                return False
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
    def save_to_file(self):
        data_dict = {}
        data_dict[self.username] = {self.__phone : self.__password}
        print("Data secure : ",data_dict)
        with open("data.txt", "a") as file:
            for key, value in data_dict.items():
                file.write('%s' %(key))
                for key, value in value.items():
                    file.write('%s %s\n' %(key, value))
    def display_details(self):
        print(f"Username: {self.username}")
        print(f"Phone: {self.__phone}")
        print(f"Encrypted Password: {self.__password}")
password = "R@m@_f0rtu9e$"
user1 = Register("Rathanak_cam",password ,85976899776)
user1.pass_strength(password)
user1.display_details()
user1.save_to_file()
print("User already exist : {}".format(user1.check_user()))


import hashlib
class Login:
    def __init__(self,username, password):
        self.username = username
        self.__password = self.encrypt_password(password)
    def encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    def check_password(self):
        try:
            file_path = "D:\G2_T1_Project\Data\data.txt"
            with open(file_path, "r") as file:
                stored_data = f"{self.username} : {self.__password}"
                for line in file:
                    if line.strip() == stored_data:
                        print("Login Successful")
                        return True
                    else:
                        print("Login Unsuccessful")
                        return False
        except FileNotFoundError:
            print("Error file is not found.")
            return False
        except IOError:
            print("An error occurred while reading the file.")
            return False
account_login = Login("phanphouth", "R@m@_f0rtu9e$")
account_login.check_password()

        
            
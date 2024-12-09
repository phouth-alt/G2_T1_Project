import hashlib
class Login:
    def __init__(self,username, password):
        self.username = username
        self.__password = self.encrypt_password(password)
    def encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    def check_password(self):
        max_attempt = 3
        attempt = 0
        try:
            with open("D:/Coding beginner/G2_T1_Project/Data/data.txt", "r") as file:
                stored_data = f"{self.username} : {self.__password}"
                while attempt < max_attempt:
                    for line in file:
                        if line.strip() == stored_data:
                            print("Login Successful")
                            return True
                    attempt += 1
                    print(f"Login Unsuccessful. Attempt remain: {max_attempt - attempt}")
                else:
                    print("No more attempts for a day!")
                    return False
        except FileNotFoundError:
            print("Error file is not found.")
            return False
        except IOError:
            print("An error occurred while reading the file.")
            return False
account_login = Login("rathanak_cam", "R@m@_f0rtu9e$")
account_login.check_password()

        
            
from encrypt_pass import encrypt_password
from check_username import check_password
def login(username,password):
        try:
            if check_password(username,password):
                 print("Login successfully")
            else:
                 print("please try again")
        except FileNotFoundError:
            print("Error file is not found.")
            return False
        except IOError:
            print("An error occurred while reading the file.")
            return False

        
            
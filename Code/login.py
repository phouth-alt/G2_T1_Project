from encrypt_pass import encrypt_password
def login(username,password):
        try:
            file_path = "D:\G2_T1_Project\Data\data.txt"
            en_password = encrypt_password(password)
            with open(file_path, "r") as file:
                for line in file:
                    parts = line.strip().split("\t\t")
                    if len(parts) > 1:
                        if parts[0] == username and parts[2] == en_password:
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

        
            
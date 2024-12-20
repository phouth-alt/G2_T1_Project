from encrypt_pass import encrypt_password
def check_username(phone):
     try:
          file_path = "data.txt"
          phone = str(phone)
          with open(file_path, 'r') as file:
               for line in file:
                    parts = line.strip().split("\t\t")
                    if len(parts) > 1:
                         if parts[1].strip() == phone:
                              return True
          return False
     except FileNotFoundError:
        print("Error: File not found at {}".format(file_path))
     
def check_user(username,password):
     try:
          en_password = encrypt_password(password)
          file_path = "data.txt"
          with open(file_path, 'r') as file:
               for line in file:
                    parts = line.strip().split("\t\t")
                    if len(parts) > 2:
                         if parts[0].strip() == username and parts[2].strip() == en_password:
                              return True
          return False
     except FileNotFoundError:
        print("Error: File not found at {}".format(file_path))

def check_password(username,password):
          try:
               file_path = "data.txt"
               en_password = encrypt_password(password)
               with open(file_path, "r") as file:
                    for line in file:
                         parts = line.strip().split("\t\t")
                         if len(parts) > 1:
                              if parts[0] == username and parts[2] == en_password:
                                   return True
               return False
          except FileNotFoundError:
               print("Error file is not found.")
               return False
          except IOError:
               print("An error occurred while reading the file.")
               return False

from encrypt_pass import encrypt_password
def check_username(phone):
     try:
          file_path = "D:\G2_T1_Project\Data\data.txt"
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
          print(en_password)
          file_path = "D:\G2_T1_Project\Data\data.txt"
          with open(file_path, 'r') as file:
               for line in file:
                    parts = line.strip().split("\t\t")
                    print(parts[0])
                    print(parts[2])
                    if len(parts) > 2:
                         if parts[0].strip() == username and parts[2].strip() == en_password:
                              return True
          return False
     except FileNotFoundError:
        print("Error: File not found at {}".format(file_path))

print(check_user("Phan Phouth","UareMYfarVoritH00@"))
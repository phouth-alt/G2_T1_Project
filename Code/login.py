from encrypt_pass import encrypt_password
from check_username import check_password

def create_user(username, password):
    file_path = "data.txt"
    try:
        en_password = encrypt_password(password)
        with open(file_path, "a") as file:  # 'a' mode appends to the file
            file.write(f"{username}\t{en_password}\n")
        print("User created successfully.")
    except IOError:
        print("An error occurred while writing to the file.")

def login(username, password):
    if check_password(username, password):
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

        
            
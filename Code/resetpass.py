from encrypt_pass import encrypt_password
from check_username import check_user

def reset_pass(username,password):
    try:
        print(check_user(username,password))
        en_password = encrypt_password(password)
        if check_user(username,password):
            password = input("New password: ")
            password = encrypt_password(password)
        else:
            print("Please try again")
            return
        file_path = "D:\G2_T1_Project\Data\data.txt"
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split("\t\t")
                if len(parts) > 2:
                    if parts[0].strip() == username.strip() and parts[2].strip() == en_password.strip():
                        
                    
    except:
        pass
    


reset_pass("Phan Phouth","UareMYfarVoritH00@")
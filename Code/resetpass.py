from encrypt_pass import encrypt_password
from check_username import check_user

def reset_pass(username,password):
    try:
        print(check_user(username,password))
    except:
        pass
    if check_user(username,password):
        password = input("New password: ")
    else:
        print("Please try again")


reset_pass("Phan Phouth","UareMYfarVoritH00@")
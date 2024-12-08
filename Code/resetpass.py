from encrypt_pass import encrypt_password
from check_username import check_user

def reset_pass(username,password):
    try:
        check_user(username,password)
    except:
        pass


reset_pass("Phan Phouth","UareMYfarVoritH00@")
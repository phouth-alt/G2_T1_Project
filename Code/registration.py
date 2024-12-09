from check_username import check_username
from pass_strength import pass_strength
from save_to_file import save_to_file
def register(username,password,phone):
    if not username or not password or not phone:
        print("Error : All fields (username, password, phone) are required.")
        return
    if check_username(phone) == True:
        print("your alread have an account. please login")
        return
    if not pass_strength(password):
        return
    save_to_file(username,password,phone)

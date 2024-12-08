from check_username import check_username
from pass_strength import pass_strength
from save_to_file import save_to_file
from encrypt_pass import encrypt_password
def register(username,password,phone):
    if check_username(phone):
        return
    if not pass_strength(password):
        return
    encrypt_password(password)
    save_to_file(username,password,phone)

username = input("Enter your full name:")
password = input("Enter password:")
phone = input("phone number: ")
register(username,password,phone)
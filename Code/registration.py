import check_username
import pass_strength
import save_to_file
import encrypt_pass
def register(username,password,phone):
    if check_username(phone):
        return
    if not pass_strength(password):
        return
    encrypt_pass(password)
    save_to_file(username,password,phone)

username = input("Enter your full name:")
password = input("Enter password:")
phone = input("phone number: ")
register(username,password,phone)
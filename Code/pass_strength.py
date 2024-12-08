import re
def pass_strength(password):
        if(len(password) <= 8):
            print("Must be longer than 8 characters.")
        elif not re.search("[a-z]",password):
            print("Must contain at least one lowercase letter.")
        elif not re.search("[A-Z]",password):
            print("Must contain at least one uppercase letter.")
        elif not re.search("[0-9]",password):
            print("Must contain at least on digit.")
        elif not re.search("[!@#$%^&*()]",password):
            print("Must contain at least one special character(!@#$%^&*()).")
        elif re.search("\s",password):
            print("Must not contain whitespace.")
        else:
            print("Valid Password")

        

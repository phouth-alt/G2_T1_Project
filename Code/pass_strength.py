import re
def pass_strength(password):
        if(len(password) <= 8):
            print("Must be longer than 8 characters.")
            return False
        elif not re.search("[a-z]",password):
            print("Must contain at least one lowercase letter.")
            return False
        elif not re.search("[A-Z]",password):
            print("Must contain at least one uppercase letter.")
            return False
        elif not re.search("[0-9]",password):
            print("Must contain at least on digit.")
            return False
        elif not re.search("[!@#$%^&*()]",password):
            print("Must contain at least one special character(!@#$%^&*()).")
            return False
        elif re.search("\s",password):
            print("Must not contain whitespace.")
            return False
        else:
            print("Valid Password")

        

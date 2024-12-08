def change_password(username, old_password, new_password):  
    """Change the user's password if the old password matches."""  
    updated = False  
    users = []  
    
    try:  
        with open('users.txt', 'r') as file:  
            users = file.readlines()  

        with open('users.txt', 'w') as file:  
            for user in users:  
                stored_username, stored_password, key_pin = user.strip().split(',')  
                if stored_username == username and stored_password == old_password:  
                    file.write(f"{stored_username},{new_password},{key_pin}\n")  
                    print("Password changed successfully.")  
                    updated = True  
                else:  
                    file.write(user)  
                    
        if not updated:  
            print("Old password is incorrect. Password change failed.")  
    
    except FileNotFoundError:  
        print("No users registered yet.") 
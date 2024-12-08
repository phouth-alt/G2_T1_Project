from pathlib import Path
def save_to_file(username,password,phone):
        if not username or not password or not phone:
             print("Error : All fields are required.")
             return
        try:
            data_dict = {}
            data_dict[username] = {phone : password}
            print("Secure Data : ",data_dict)
            with open("file_to_open", "a") as file:
                for username, details in data_dict.items():
                    for phone, password in details.items():
                        file.write('%s\t%s\t%s\n' %(username,phone, password))
            print("Save to file completed successfully.")
        except IOError as e: 
             print("File error: {}".format(e))
        finally:
             print("Execution of Save to file completed.")
username = input("Full Name:")
password = input("Enter Pasword:")
phone = input("phone number")
save_to_file(username,password,phone)


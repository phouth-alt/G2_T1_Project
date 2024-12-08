
def save_to_file(username,password,phone):
        if not username or not password or not phone:
             print("Error : All fields (username, password, phone) are required.")
             return
        try:
            data_dict = {}
            data_dict[username] = {phone : password}
            file_path = "D:\G2_T1_Project\Data\data.txt"
            print("Secure Data : ",data_dict)
            with open(file_path, "a") as file:
                for username, details in data_dict.items():
                    for phone, password in details.items():
                        file.write('%s\t\t%s\t\t%s\n' %(username,phone, password))
            print("Save to file completed successfully.")
        except IOError as e: 
             print("File error: {}".format(e))
        finally:
             print("Execution of Save to file completed.")
username = input("Full Name: ")
password = input("Enter Pasword: ")
phone = input("phone number: ")
save_to_file(username,password,phone)


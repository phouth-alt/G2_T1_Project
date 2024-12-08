from encrypt_pass import encrypt_password
def check_username(phone):
     try:
          file_path = "D:\G2_T1_Project\Data\data.txt"
          phone = str(phone)
          with open(file_path, 'r') as file:
               for line in file:
                    parts = line.strip().split("\t\t")
                    if len(parts) > 1:
                         if parts[1].strip() == phone:
                              return True
          return False
     except FileNotFoundError:
        print("Error: File not found at {}".format(file_path))

def check_user(username, password):
    try:
        # Encrypt the password for comparison
        encrypted_password = encrypt_password(password)
        
        # Use a raw string for the file path
        file_path = r"D:\G2_T1_Project\Data\data.txt"
        
        # Open and read the file
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split("\t\t")  # Use correct delimiter
                if len(parts) > 2:  # Ensure the line has at least 3 parts
                    if parts[0].strip() == username and parts[2].strip() == encrypted_password:
                        return True  # Username and password match
            
        # If no match found
        return False
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
print(check_user("Phan Phouth", "UareMYfarVoritH00@"))

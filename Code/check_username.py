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
     finally:
          print("check user operation completed.\n")


def check_user(phones):
     file_path = "D:\G2_T1_Project\Data\data.txt"
     with open(file_path, 'r') as file:
          for line in file:
               parts = line.strip().split("\t\t")
               if len(parts) > 1 and parts[1].strip() == phones:
                    return True
               else:
                    return False
               


print(check_user(85939849383))

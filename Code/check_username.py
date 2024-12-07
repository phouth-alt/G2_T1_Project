def check_user(phones):
        with open("data.txt", 'r') as file:
           for line in file:
                parts = line.strip().split("\t")
                parts = [part for part in parts if part]
                if len(parts) >= 2:
                    phone = parts[1]
                    if phone == phones:
                         return True
                    else:
                         return False
                else:
                    print(f"Invalid line format: {line.strip()}")


print(check_user(85939849383))

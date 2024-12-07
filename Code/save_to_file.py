def save_to_file(username,password,phone):
        data_dict = {}
        data_dict[username] = {phone : password}
        print("Data secure : ",data_dict)
        with open("test.txt", "a+") as file:
            for keys, values in data_dict.items():
                for key, value in values.items():
                    file.write('%s\t\t\t\t%s\t\t\t\t%s\n' %(keys,key, value))
                    
save_to_file("phanphouth","oekjsuje0398",39848383922)


import re
def pass_strength(self):
    flag = 0
    while True:
        if(len(self.__password) < 8):
            flag = -1
            break
        elif not re.search("[a-z]", self.__password):
            flag = -1
            break
        elif not re.search("[A-Z]", self.__password):
            flag = -1
            break
        elif not re.search("[0-9]", self.__password):
            flag = -1
            break
        elif not re.search("[!@#$%^&*()]", self.__password):
            flag = -1
            break
        elif re.search("\s", self.__password):
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password")
            break
        
    if flag == -1: 
        print("Not a Valid Password")
class AuthenticationSystem:
    def __init__(self,username,password,phone):
        self.username = username #phone number follow format +855976899776
        self.__password = password #password hash and store in dictionary after format to file
        self.__phone = phone #where we should store this one
    def Options(self):
        while True:
            print("============================================")
            print("===========Authentication System============")
            print("============================================")
            print("1.Login")
            print("2.Register")
            print("3.Reset Password")
            print("4.ForgetPassword")
            print("5.Exit program")
            print("============================================")
            print("=============Enter an option================")
            print("--------------------------------------------")
            input_options = input("")
            if input_options == '1':
                print("Didn't have action yet")
                print("\n")
            elif input_options == '2':
                print("Didn't have action yet")
                print("\n")

            elif input_options == '3':
                print("Didn't have action yet")
                print("\n")

            elif input_options == '4':
                print("Didn't have action yet")
                print("\n")

            elif input_options == '5':
                print("Exiting program successfuly")
                break
            else:
                print("invalid option, please choose options again\n")


user1 = AuthenticationSystem("phouth","iesls03",829372344)
user1.Options()
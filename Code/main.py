class AuthenticationSystem:
    def __init__(self,username,password,phone):
        self.username = username
        self.__password = password
        self.__phone = phone
    def Options(self):
        print("============================================")
        print("===========Authentication System============")
        print("============================================")
        print("1.Registration")
        print("2.Login")
        print("3.Reset Password")
        print("4.ForgetPassword")
        print("5.Exit program")
        print("============================================")
        input_options = input("Enter an option:")
        while True:
            if input_options == '1':
                print("Didn't have action yet")
                break
            elif input_options == '2':
                print("Didn't have action yet")
                break
            elif input_options == '3':
                print("Didn't have action yet")
                break
            elif input_options == '4':
                print("Didn't have action yet")
                break
            elif input_options == '5':
                print("Exiting program...")
                break
            else:
                print("invalid option, please choose options again")
                break



user1 = AuthenticationSystem("phouth","iesls03",829372344)
user1.Options()
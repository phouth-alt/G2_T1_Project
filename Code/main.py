from registration import register
class AuthenticationSystem:
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
                print("\nLogin functionality is under development.\n")
                print("\n")
            elif input_options == '2':
                first_name = input("First name:")
                last_name = input("Last name: ")
                username = first_name + " " + last_name
                password = input("Enter password:")
                phone = input("phone number: ")
                register(username,password,phone)
                print("\n")

            elif input_options == '3':
                print("\nLogin functionality is under development.\n")
                print("\n")

            elif input_options == '4':
                print("\nLogin functionality is under development.\n")
                print("\n")

            elif input_options == '5':
                print("Exiting program successfuly")
                break
            else:
                print("invalid option, please choose options again\n")


if __name__ == "__main__":
    user1 = AuthenticationSystem()
    user1.Options()
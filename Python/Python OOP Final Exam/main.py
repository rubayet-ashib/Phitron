from user import User
from admin import Admin
from panel import Panel

pan = Panel()

def create_account():
    print("### Create an account ###")
    name = input("Enter your name : ")
    email = input("Enter your email (must contain @ sign): ")
    address = input("Enter your address : ")
    acc_type = input("Enter account type (Savings / Current): ")

    usr = User(name = name, email = email, address = address, acc_type = acc_type)

    print(pan.add_user(usr))
    return usr

def user_interface():
    usr = create_account()

    while True:
        print("\n1. Create an account")
        print("2. Deposite")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Check Transaction History")
        print("6. Take a loan")
        print("7. Transfer")
        print("8. Switch mode\n")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            usr = create_account()
                
        elif choice == 2:
            amount = int(input("Enter amount : "))
            usr.deposite(pan, usr, amount)

        elif choice == 3:
            amount = int(input("Enter amount : "))
            usr.withdraw(pan, usr, amount)

        elif choice == 4:
            usr.check_balance(pan, usr)
        
        elif choice == 5:
            usr.check_trxn_history(pan, usr)

        elif choice == 6:
            amount = int(input("Enter amount : "))
            usr.take_loan(pan, usr, amount)

        elif choice == 7:
            receiver_acc = input("Enter receiver account no. : ")
            amount = int(input("Enter amount : "))
            usr.transfer(pan,usr,receiver_acc,amount)

        elif choice == 8:
            return

        else:
            print("\nInvalid input!")

def admin_interface():
    admin = Admin()

    while True:
        print("\n1. Create an account")
        print("2. Delete an account")
        print("3. Show all user accounts list")
        print("4. Check total available balance of the bank")
        print("5. Check total loan amount")
        print("6. Turn ON/OFF loan feature")
        print("7. Switch mode\n")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            usr = create_account()
        
        elif choice == 2:
            usr = None
            id = input("Enter user email to be deleted : ")
            for item in pan.users:
                if item.email == id:
                    usr = item
                    break

            if(usr == None):
                print("\nAccount does not exist!")
            else:
                admin.delete_user(pan, usr)
                print("\nAccount deleted successfully.")
        
        elif choice == 3:
            print("")
            admin.show_user_list(pan)
        
        elif choice == 4:
            admin.total_balance(pan)
        
        elif choice == 5:
            admin.total_loan(pan)
        
        elif choice == 6:
            print("1. ON")
            print("2. OFF")

            val = int(input("Choose : "))
            if(val == 1):
                admin.loan_feature(pan, True)
                print("\nLoan status turnned ON")
            else:
                admin.loan_feature(pan, False)
                print("\nLoan status turnned OFF")
        
        elif choice == 7:
            return

        else:
            print("\nInvalid input!")


while True:
    print("\n1. User")
    print("2. Admin")
    print("3. Exit\n")

    option = int(input("Choose your mode : "))

    if option == 1:
        user_interface()
    elif option == 2:
        admin_interface()
    elif option == 3:
        break
    else:
        print("\nInvalid input!")
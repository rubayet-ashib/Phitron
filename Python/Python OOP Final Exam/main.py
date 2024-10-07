from user import User
from admin import Admin
from panel import Panel

pan = Panel()

def create_account():
    print("### Create an account ###")
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    address = input("Enter your address : ")
    acc_type = input("Enter account type (Savings / Current): ")

    usr = User(name = name, email = email, address = address, acc_type = acc_type)
    status = pan.add_user(pan, usr)
    if(status == False):
        print("Try again!")
        create_account()
    else:
        return usr

def user_interface():
    usr = create_account()
    while True:
        print("\n1. Create an account")
        print("\n1. Sign in")
        print("2. Deposite")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Take a loan")
        print("6. Transfer")
        print("7. Exit\n")

        choice = int(input("Enter your choice : "))
        if choice == 0:
            usr = create_account()
        elif choice == 1:
            amount = int(input("Enter amount : "))
            usr.deposite(pan, usr, amount)
        elif choice == 2:
            amount = int(input("Enter amount : "))
            usr.withdraw(pan, usr, amount)
        elif choice == 3:
            usr.check_balance(pan, usr)
        elif choice == 4:
            amount = int(input("Enter amount : "))
            usr.take_loan(pan, usr, amount)
        elif choice == 5:
            receiver_acc = input("Enter receiver account no. : ")
            amount = int(input("Enter amount : "))
            usr.transfer(pan,usr,receiver_acc,amount)
        elif choice == 6:
            break
        else:
            print("Invalid input!")

user_interface()




from datetime import datetime
# from admin import Admin
# from user import User

class Panel:
    def __init__(self):
        self.users = []
        self.is_bankrupt = False
        self.total_loan = 0
        self.loan_feature = True
    
    # admin section
    def add_user(self, usr):
        for item in self.users:
            if usr.acc_no == item.acc_no:
                print("Account already exists")
                return False
            else:
                self.users.append(usr)
                print("Account created successfully!")
                return True
                

    def show_user_list(self):
        for item in self.users:
            print(f"{item.acc_no}\n{item.name}\n{item.email}\n{item.address}\n{item.acc_type}")
    
    def delete_user(self, usr):
        self.users.remove(usr)
    
    def total_balance(self):
        amount = 0
        for item in self.users:
            amount += item.balance
        
        print(f"Total available balance = {amount}")
    
    # user section
    def check_balance(self, usr):
        print(f"Current balance = {usr.balance}")
    
    def deposite(self, usr, amount):
        usr.balance += amount

        # add transaction history
        now = datetime.now()
        formatted_time = now.strftime("%A, %B %d, %Y (%I:%M %p)")

        trxn = {"Time" : formatted_time, "Type" : "Deposite"}
        usr.trxn_history.append(trxn)
    
    def withdraw(self, usr, amount):
        if(usr.balance >= amount and self.is_bankrupt == False):
            usr.balance -= amount

            # add transaction history
            now = datetime.now()
            formatted_time = now.strftime("%A, %B %d, %Y (%I:%M %p)")

            trxn = {"Time" : formatted_time, "Type" : "Withdraw"}
            usr.trxn_history.append(trxn)

        else:
            print("Withdrawal amount exceeded")

    def take_loan(self, usr, amount):
        if(self.loan_feature == False):
            print("Loan feature turnned off!")
        elif(usr.loan_count):
            usr.balance += amount
            self.total_loan += amount
            usr.loan_count -= 1
        else:
            print("Loan limit exceeded")
    
    def transfer(self, sender, receiver_acc, amount):
        receiver = ""
        found = False
        for item in self.users:
            if receiver_acc == item.acc_no:
                found = True
                receiver = item

        if (found == False):
            print("Account does not exist")
        else:
            if(sender.balance >= amount):
                sender.balance -= amount
                receiver.balance += amount

                # add transaction history
                now = datetime.now()
                formatted_time = now.strftime("%A, %B %d, %Y (%I:%M %p)")

                trxn = {"Time" : formatted_time, "Type" : "Transfer", "Sender AC/No" : sender.acc_no, "Receiver AC/No" : receiver.acc_no}
                sender.trxn_history.append(trxn)

            else:
                print("Not enough money")
    
    def check_trxn_history(self, usr):
        for i in range(len(usr.trxn_history)):
            print(f"{i+1}. ")
            for key, value in usr.trxn_history[i].items():
                print(f"{key} : {value}")
            print("")
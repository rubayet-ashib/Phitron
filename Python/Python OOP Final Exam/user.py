from abc import ABC

class Person(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class User(Person):
    def __init__(self, name, email, address, acc_type):
        super().__init__(name, email, address)
        self.acc_no = email[:email.find('@')].upper()
        self.acc_type = acc_type
        self.balance = 0
        self.trxn_history = []
        self.loan_count = 2
    
    def add_user(self, panel, usr):
        panel.add_user(usr)
    
    def check_balance(self, panel, usr):
        panel.check_balance(usr)
    
    def deposite(self, panel, usr, amount):
        panel.deposite(usr, amount)

    def withdraw(self, panel, usr, amount):
        panel.withdraw(usr, amount)
    
    def take_loan(self, panel, usr, amount):
        panel.take_loan(usr, amount)
    
    def transfer(self, panel, from_user, receiver_acc, amount):
        panel.transfer(from_user, receiver_acc, amount)
    
    def check_trxn_history(self, panel, usr):
        panel.check_trxn_history(usr)
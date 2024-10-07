from abc import ABC
# from user import User
# from panel import Panel

class Person(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Admin(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
    
    def add_user(self, panel, usr):
        panel.add_user(usr)

    def show_user_list(self, panel):
        panel.show_user_list()

    def delete_user(self, panel, usr):
        panel.delete_user(usr)
    
    def total_balance(self, panel):
        panel.total_balance()
    
    def total_loan(self, panel):
        print(f"Total loan amount = {panel.total_loan}")
    
    def loan_feature(self, panel, feature):
        if(feature == 0):
            panel.loan_feature = False
        else:
            panel.loan_feature = True
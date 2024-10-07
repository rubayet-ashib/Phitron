class Admin:

    def __init__(self) -> None:
        pass

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
        panel.loan_feature = feature
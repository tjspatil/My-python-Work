class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, add_money):
        self.balance = self.balance + add_money
        print("fund credited")
    
    def withdraw(self, out_money):
        if self.balance > out_money:
            self.balance = self.balance - out_money
            print("fund debited, your available balance is {}" .format(self.balance))
        else:
            print("low balance! you can debit maximum {} from your account" .format(self.balance))

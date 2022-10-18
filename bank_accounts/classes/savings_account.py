from account import Account
class CheckingAccount(Account):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.check_uses=0
    
    def withdraw(self, amount):
        if self.balance-amount-1<0:
            raise Exception("Sorry, not enough money to withdraw")
        self.balance = self.balance - amount-1
        print(f"Your balance is now {self.balance}")
    
    def withdraw_using_check(self, amount):
        if self.balance-amount<-10:
            raise Exception("Sorry, not enough money to withdraw")
        if self.check_uses<=3:
            self.balance=self.balance-amount
        else:
            self.balance=self.balance-amount-2
        self.check_uses+=1
    def reset_checks(self):
        self.check_uses=0
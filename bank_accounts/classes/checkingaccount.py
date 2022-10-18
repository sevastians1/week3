from account import Account
class SavingsAccount(Account):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def balance(self, balance):
        if balance<10:
            raise Exception("Sorry, intial balance must be above 10")
        return balance

    def withdraw(self, amount):
        if self.balance-amount<10:
            raise Exception("Sorry, not enough money to withdraw")
        self.balance = self.balance - amount -2
        print(f"Your balance is now {self.balance}")

    def add_interest(self, rate):
        self.balance = self.balance*rate+self.balance



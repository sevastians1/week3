from account import Account
class MoneyMarketAccount(Account):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_transaction_num=0
        self.account_locked=False

    def balance(self, balance):
        if balance<10000:
            raise Exception("Sorry, no numbers below zero")
        return balance

    def withdraw(self, amount):
        print(self.account_locked)
        if self.account_locked:
            print("Maximum transactions or account locked")
        elif self.balance-amount<10000:
            self.balance = self.balance - amount-100
            self.account_locked=True
            print(f"Your balance is now {self.balance} and your account is locked")
            self.max_transaction_num+=1

        else:
            self.balance = self.balance - amount
            print(f"Your balance is now {self.balance}")
            self.max_transaction_num+=1
            if self.max_transaction_num>=6:
                self.account_locked=True

    def depost(self, amount):
        if self.account_locked and amount+self.balance >10000 and self.balance<10000:
                self.balance = self.balance + amount
                print(f"Your balance is now {self.balance}")
                if self.max_transaction_num>6:
                    self.account_locked=False
        elif self.account_locked==True:
            print("Maximum transactions")
        else:
            self.balance = self.balance + amount
            print(f"Your balance is now {self.balance}")
            self.max_transaction_num+=1
            if self.max_transaction_num>6:
                self.account_locked=True
    def add_interest(self, rate):
        self.balance = self.balance*rate+self.balance
    def reset_transactions(self):
        self.max_transaction_num=0
        self.account_locked=False


# Bob=MoneyMarketAccount(**{"id":1717, "balance":12326, "account_created":"some_date"})
# Bob.withdraw(5)
# Bob.withdraw(5)
# Bob.withdraw(5)
# Bob.withdraw(5)
# Bob.withdraw(5)
# Bob.withdraw(5)
# print(Bob.max_transaction_num, Bob.account_locked)
# Bob.withdraw(5)
# print(Bob.max_transaction_num, Bob.account_locked)
# Bob.depost(20)

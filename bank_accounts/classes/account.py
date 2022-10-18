# from owner import Owner
import csv
class Account:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.date_opened=kwargs["account_created"]
        self.balance = self.balance(int(kwargs["balance"]))
        self.owner=None
    current_accounts=None

    def balance(self, balance):
        if balance<0:
            raise Exception("Sorry, no numbers below zero")
        return balance

    def withdraw(self, amount):
        if self.balance-amount<0:
            raise Exception("Sorry, not enough money to withdraw")
        self.balance = self.balance - amount
        print(f"Your balance is now {self.balance}")

    def depost(self, amount):
        self.balance = self.balance + amount
        print(f"Your balance is now {self.balance}")
    
    def __str__(self):
        return str(f"Your balance is now {self.balance}")

    @classmethod
    def all_accounts(cls):
        list_of_accounts=[]
        with open("assignments/bank_accounts/data/accounts.csv", "r") as f:
            for row in f:
                split=row.split(",")
                dict_of_data={}
                for count, y in enumerate(split):
                    if count==0:
                        dict_of_data["id"]=int(y)
                    if count==1:
                        # print(y)
                        dict_of_data["balance"]=int(y)*.01
                        # print(int(y)*.01)
                    if count==2:
                        dict_of_data["account_created"]=y.replace("\n", "")
                # print(dict_of_data)
                list_of_accounts.append(Account(**dict_of_data))
        cls.current_accounts=list_of_accounts
        # print(cls.current_accounts)
        return list_of_accounts

    @classmethod
    def get_account_by_id(cls, id):
        # list_of_accounts=cls.all_accounts()
        for account in cls.current_accounts:
            # print(account.id)
            if account.id==id:
                # print(f"Your account is balance is {account.balance}")
                return account




# Bob=Account(**{"id":1717, "balance":6.45, "account_created":"some_date"})
# Bob.withdraw(2.02)
# Account.all_accounts()
# Account.get_account_by_id("1217")
# print(Bob.all_accounts())
# print(Account.current_accounts)
# print(Bob.current_accounts)
from classes.account import Account

class Owner(Account):
    current_owners=None
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.l_name = kwargs["l_name"]
        self.f_name = kwargs["f_name"]
        self.address = kwargs["address"]
        self.city = kwargs["city"]
        self.state = kwargs["state"]
        self.subordinate_accounts=[]
    
    def add_owner_to_account(self, account):
        self.subordinate_accounts.append(account)
        account.owner = self.f_name+" "+self.l_name

    @classmethod
    def all_accounts(cls):
        list_of_owners=[]
        with open("assignments/bank_accounts/data/owners.csv", "r") as f:
            for row in f:
                split=row.split(",")
                dict_of_data={}
                for count, y in enumerate(split):
                    if count==0:
                        dict_of_data["id"]=int(y)
                    elif count==1:
                        dict_of_data["f_name"]=y
                    elif count==2:
                        dict_of_data["l_name"]=y
                    elif count==3:
                        dict_of_data["address"]=y
                    elif count==4:
                        dict_of_data["city"]=y
                    elif count==5:
                        dict_of_data["state"]=y.replace("\n", "")
                # print(dict_of_data)
                list_of_owners.append(Owner(**dict_of_data))
        cls.current_accounts=list_of_owners
        # print(cls.current_accounts)
        return list_of_owners

    @classmethod
    def get_account_by_id(cls, id):
        current_owners=cls.all_accounts()
        for account in current_owners:
            # print(account.id)
            if account.id==id:
                return account

    @classmethod
    def connect_accounts(cls):
        ##takes both id's, pulls both accounts, and calls owner add method, changing the owner and adding account to their list
        with open("assignments/bank_accounts/data/account_owners.csv", "r") as f:
            Account.all_accounts()
            for row in f:
                split=row.split(",")
                row=[int(split[0]), int(split[1].replace("\n", ""))]
                # print(row[0], row[1])
                account=Account.get_account_by_id(row[0])
                owner=Owner.get_account_by_id(row[1])
                owner.add_owner_to_account(account)
                # print(account.owner)

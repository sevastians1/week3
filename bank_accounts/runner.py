
from classes.owner import Owner
# from classes.account import Account
object={
        "l_name":"Boss",
        "f_name":"billy",
        "address":"1234 Way",
        "city":"city",
        "state":"WA",
        'id':"1231"}
Boss=Owner(**object)
# Owner.get_account_by_id(25)
Owner.connect_accounts()
# Boss.add_owner_to_account(Bob)
# print(Boss.subordinate_accounts)
# print(Bob.owner)
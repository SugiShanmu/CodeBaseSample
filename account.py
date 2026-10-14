import json

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def load_accounts(self):
        # BUG: RESOURCE_LEAK - file + json resource
        f = open('accounts.json')
        data = json.load(f)
        # f never closed
        for acc in data:
            self.accounts[acc['id']] = acc
        return self.accounts

    def get_balance(self, account_obj):
        # BUG: account_obj and account_obj.owner both can be None
        owner_name = account_obj.owner.name
        balance = account_obj.balance
        print(f"Balance for {owner_name}: {balance}")
        return balance

    def close_account(self, acc):
        # BUG: nested null dereference
        if acc.details.status == "ACTIVE":
            acc.details.status = "CLOSED"
            # BUG: file leak
            log = open('account_close.log', 'a')
            log.write(f"Closed {acc.id}\n")
            # not closed
from savings_account import SavingsAccount
from current_account import CurrentAccount


class AccountFactory:

    @staticmethod
    def create(kind, owner, account_number, balance, value):
        if kind == "savings":
            return SavingsAccount(owner, account_number, balance, value)

        if kind == "current":
            return CurrentAccount(owner, account_number, balance, value)
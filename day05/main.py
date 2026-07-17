from account import Account
from savings_account import SavingsAccount
from current_account import CurrentAccount


account1 = SavingsAccount(
    "Tsion",
    "001",
    1000,
    0.05
)


account2 = CurrentAccount(
    "Abel",
    "002",
    500,
    300
)


accounts = [account1, account2]


account1.add_interest()

account2.withdraw(700)


for account in accounts:
    account.statement()
    print()
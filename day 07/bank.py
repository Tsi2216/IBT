from account_factory import AccountFactory
from sms_alert import SMSAlert


alert = SMSAlert()

account1 = AccountFactory.create(
    "savings",
    "Tsion",
    "001",
    1000,
    0.05
)

account2 = AccountFactory.create(
    "current",
    "Abel",
    "002",
    500,
    300
)

account1.subscribe(alert)
account2.subscribe(alert)

accounts = [account1, account2]

account1.add_interest()

account2.withdraw(700)

for account in accounts:
    account.statement()
    print()
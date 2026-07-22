from account_factory import AccountFactory
from sms_alert import SMSAlert
from registry import AccountRegistry

alert = SMSAlert()
registry = AccountRegistry()

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

registry.add(account1)
registry.add(account2)

account1.add_interest()
account2.withdraw(700)

account1.undo_last()
account2.undo_last()

for account in registry.list_all():
    account.statement()
    print()
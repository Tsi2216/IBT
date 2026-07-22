class AccountRegistry:
    def __init__(self):
        self.by_number = {}
        self.order = []

    def add(self, acc):
        self.by_number[acc.account_number] = acc
        self.order.append(acc.account_number)

    def find(self, number):
        return self.by_number.get(number)

    def list_all(self):
        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts


class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def undo_last(self):
        if self.history:
            action, amount = self.history.pop()

            if action == "deposit":
                self.balance -= amount

            elif action == "withdraw":
                self.balance += amount


account1 = Account("Almaz", "1001", 1000)
account2 = Account("Dawit", "1002", 500)

registry = AccountRegistry()

registry.add(account1)
registry.add(account2)

account1.deposit(200)
account1.withdraw(100)

print(registry.find("1001").owner)

for account in registry.list_all():
    print(account.owner, account.balance)

account1.undo_last()

print(account1.balance)
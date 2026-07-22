from account import Account


class CurrentAccount(Account):

    def __init__(self, owner, account_number, balance, overdraft):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self._Account__balance -= amount
            self.history.append(("withdraw", amount))
            print("Withdrawal completed")
            self.notify("Withdrawal completed")
        else:
            print("Overdraft limit exceeded")

    def statement(self):
        print("Current Account")
        super().statement()
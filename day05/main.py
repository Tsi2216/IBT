class Account:
    def init(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid withdrawal.")

    def statement(self):
        print(f"Account: {self.owner} - Balance: {self._balance}")


class SavingsAccount(Account):
    def init(self, owner, account_number, balance=0, rate=0.05):
        super().init(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        self._balance += self._balance * self.rate

    def statement(self):
        print(f"Savings Account: {self.owner} - Balance: {self._balance}")


class CurrentAccount(Account):
    def init(self, owner, account_number, balance=0, overdraft=500):
        super().init(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance + self.overdraft:
            self._balance -= amount
        else:
            print("Overdraft limit exceeded.")

    def statement(self):
        print(f"Current Account: {self.owner} - Balance: {self._balance}")


acc1 = Account("Abel", "1001", 1000)
acc2 = SavingsAccount("Sara", "1002", 2000)
acc3 = CurrentAccount("John", "1003", 500)

acc2.add_interest()
acc3.withdraw(800)

accounts = [acc1, acc2, acc3]

for account in accounts:
    account.statement()
class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000

        return cls._instance


class SMSAlert:
    def update(self, message):
        print("SMS Alert:", message)


class AuditLog:
    def update(self, message):
        print("Audit Log:", message)


class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

        self.observers = []
        self.history = []

    @property
    def balance(self):
        return self.__balance

    def subscribe(self, observer):
        self.observers.append(observer)

    def _notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount

        self.history.append(
            ("deposit", amount)
        )

        self._notify("Deposit completed")


    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount

        self.history.append(
            ("withdraw", amount)
        )

        self._notify("Withdrawal completed")


    def undo_last(self):

        if self.history:

            action, amount = self.history.pop()

            if action == "deposit":
                self.__balance -= amount

            elif action == "withdraw":
                self.__balance += amount


    def statement(self):

        print("Account")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")



class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(owner, number, balance)

        self.rate = BankConfig().interest_rate


    def add_interest(self):

        self.deposit(
            self.balance * self.rate
        )


    def statement(self):

        print("Savings Account")
        super().statement()



class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(owner, number, balance)

        self.overdraft = BankConfig().overdraft_limit



    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")


        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded")


        self._Account__balance -= amount


        self.history.append(
            ("withdraw", amount)
        )


        self._notify("Withdrawal completed")



    def statement(self):

        print("Current Account")
        super().statement()



class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":

            return SavingsAccount(
                owner,
                number,
                balance
            )


        elif kind == "current":

            return CurrentAccount(
                owner,
                number,
                balance
            )


        else:

            raise ValueError("Unknown account type")



# Day 7 addition

class AccountRegistry:

    def __init__(self):

        self.by_number = {}

        self.order = []


    def add(self, account):

        self.by_number[
            account.account_number
        ] = account


        self.order.append(
            account.account_number
        )


    def find(self, number):

        return self.by_number.get(number)



    def list_all(self):

        accounts = []

        for number in self.order:

            accounts.append(
                self.by_number[number]
            )

        return accounts



# Test

registry = AccountRegistry()


account1 = AccountFactory.create(
    "savings",
    "Almaz",
    "1001",
    1000
)


account2 = AccountFactory.create(
    "current",
    "Dawit",
    "1002",
    500
)



sms = SMSAlert()

audit = AuditLog()



account1.subscribe(sms)

account1.subscribe(audit)



registry.add(account1)

registry.add(account2)



account1.deposit(500)

account1.withdraw(200)



print(
    registry.find("1001").owner
)



for account in registry.list_all():

    account.statement()



account1.undo_last()



print(
    "After undo:",
    account1.balance
)
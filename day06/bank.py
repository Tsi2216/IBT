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
        print("SMS:", message)


class AuditLog:
    def update(self, message):
        print("Audit:", message)


class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self._balance = balance
        self.observers = []

    @property
    def balance(self):
        return self._balance

    def subscribe(self, observer):
        self.observers.append(observer)

    def _notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        self._notify("Deposit completed")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._notify("Withdrawal completed")

    def statement(self):
        print(self.owner, self.account_number, self.balance)


class SavingsAccount(Account):
    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.rate = BankConfig().interest_rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)


class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.overdraft = BankConfig().overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amount
        self._notify("Withdrawal completed")


class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        elif kind == "current":
            return CurrentAccount(owner, number, balance)
        else:
            raise ValueError("Unknown account type")


account1 = AccountFactory.create("savings", "Almaz", "1001", 1000)
account2 = AccountFactory.create("current", "Dawit", "1002", 500)

sms = SMSAlert()
audit = AuditLog()

account1.subscribe(sms)
account1.subscribe(audit)

account1.deposit(500)
account1.statement()
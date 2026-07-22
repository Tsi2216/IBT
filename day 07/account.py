class Account:

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.observers = []
        self.history = []

    @property
    def balance(self):
        return self.__balance

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.history.append(("deposit", amount))
            self.notify("Deposit completed")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.history.append(("withdraw", amount))
            self.notify("Withdrawal completed")
        else:
            print("Insufficient funds")

    def undo_last(self):
        if self.history:
            self.history.pop()

    def statement(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)
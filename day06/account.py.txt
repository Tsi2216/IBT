class Account:

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.observers = []

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
            self.notify("Deposit completed")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.notify("Withdrawal completed")
        else:
            print("Insufficient funds")

    def statement(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)
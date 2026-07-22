class Account:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount


account1 = Account("Almaz", "1001", 1000)
account2 = Account("Dawit", "1002", 500)

account1.deposit(500)
account1.withdraw(200)

account2.deposit(300)
account2.withdraw(1000)

print(account1.owner, account1.balance)
print(account2.owner, account2.balance)
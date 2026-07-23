class Account:

    def __init__(self, owner, account_number, balance=0):
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
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")

        elif amount > self.__balance:
            print("Insufficient balance.")

        else:
            self.__balance -= amount


account1 = Account("Abel", "1001", 1000)
account2 = Account("Sara", "1002", 500)

account1.deposit(500)
account1.withdraw(200)

account2.deposit(300)
account2.withdraw(1000)

print(account1.owner, account1.balance)
print(account2.owner, account2.balance)
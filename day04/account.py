class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than 0.")
            return

        self.__balance += amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount
        print(f"Withdrew ${amount}")

    def statement(self):
        print("------------------------")
        print("Account Statement")
        print("------------------------")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance)
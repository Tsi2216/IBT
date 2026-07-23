class Account:

    def __init__(self, owner, number, balance=0):

        self.owner = owner
        self.account_number = number
        self.__balance = balance

        self.history = []


    @property
    def balance(self):
        return self.__balance



    def deposit(self, amount):

        self.__balance += amount

        self.history.append(
            ("deposit", amount)
        )



    def withdraw(self, amount):

        self.__balance -= amount

        self.history.append(
            ("withdraw", amount)
        )



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



    # Day 8 addition
    def top_by_balance(self, n=5):

        accounts = sorted(
            self.by_number.values(),
            key=lambda a: a.balance,
            reverse=True
        )

        return accounts[:n]



    def find_by_number(self, number):

        nums = sorted(self.by_number)

        index = binary_search(nums, number)


        if index >= 0:

            return self.by_number[
                nums[index]
            ]

        return None



    def total_transactions(self, number):

        account = self.find_by_number(number)


        if account is None:
            return 0


        def recursive_sum(history):

            if len(history) == 0:
                return 0


            return history[0][1] + recursive_sum(
                history[1:]
            )


        return recursive_sum(account.history)



def binary_search(items, target):

    left = 0
    right = len(items) - 1


    while left <= right:

        middle = (left + right) // 2


        if items[middle] == target:
            return middle


        elif items[middle] < target:
            left = middle + 1


        else:
            right = middle - 1


    return -1



# Test


account1 = Account(
    "Almaz",
    "1001",
    1000
)


account2 = Account(
    "Dawit",
    "1002",
    2000
)


account3 = Account(
    "Hanna",
    "1003",
    500
)



account1.deposit(300)
account1.withdraw(100)


registry = AccountRegistry()


registry.add(account1)
registry.add(account2)
registry.add(account3)



print("Search:")
print(
    registry.find_by_number("1002").owner
)



print("\nLeaderboard:")

for account in registry.top_by_balance(2):

    print(
        account.owner,
        account.balance
    )



print("\nTransactions:")
print(
    registry.total_transactions("1001")
)
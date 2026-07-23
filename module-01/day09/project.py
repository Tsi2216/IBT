from collections import deque


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
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        self.__balance -= amount
        self.history.append(("withdraw", amount))


class AccountRegistry:
    def __init__(self):
        self.by_number = {}
        self.order = []

    def add(self, account):
        self.by_number[account.account_number] = account
        self.order.append(account.account_number)

    def top_by_balance(self, n=5):
        accounts = sorted(
            self.by_number.values(),
            key=lambda a: a.balance,
            reverse=True
        )
        return accounts[:n]

    def find_by_number(self, number):
        numbers = sorted(self.by_number)

        index = binary_search(numbers, number)

        if index >= 0:
            return self.by_number[numbers[index]]

        return None

    def total_transactions(self, number):
        account = self.find_by_number(number)

        if account is None:
            return 0

        def total(history):
            if not history:
                return 0

            return history[0][1] + total(history[1:])

        return total(account.history)


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


# Day 9: Branch Tree

class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.accounts = []

    def total_balance(self):
        total = sum(account.balance for account in self.accounts)

        for child in self.children:
            total += child.total_balance()

        return total


head_office = Branch("Head Office")
addis_region = Branch("Addis Region")
bole_branch = Branch("Bole Branch")


account1 = Account("Almaz", "1001", 1000)
account2 = Account("Dawit", "1002", 2000)
account3 = Account("Hanna", "1003", 500)


head_office.children.append(addis_region)
addis_region.children.append(bole_branch)

head_office.accounts.append(account1)
addis_region.accounts.append(account2)
bole_branch.accounts.append(account3)


# Day 9: Transfers Graph

transfers = {
    "1001": ["1002", "1003"],
    "1002": ["1003"],
    "1003": ["1004"],
    "1004": []
}


def bfs(transfers, start):
    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)

            for receiver in transfers[current]:
                queue.append(receiver)

    return visited


print("Bank total:")
print(head_office.total_balance())

print("Accounts reachable from 1001:")
print(bfs(transfers, "1001"))
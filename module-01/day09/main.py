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
            key=lambda account: account.balance,
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
            if len(history) == 0:
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


# Day 9: Branch tree

class Branch:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.children = []

    def add_branch(self, branch):
        self.children.append(branch)

    def total_balance(self):
        total = self.balance

        for child in self.children:
            total += child.total_balance()

        return total


head_office = Branch("Head Office", 100000)

north = Branch("North Region", 50000)
south = Branch("South Region", 40000)

branch1 = Branch("Branch 1", 15000)
branch2 = Branch("Branch 2", 12000)
branch3 = Branch("Branch 3", 18000)

head_office.add_branch(north)
head_office.add_branch(south)

north.add_branch(branch1)
north.add_branch(branch2)

south.add_branch(branch3)


# Day 9: Transfers graph

transfers = {
    "CBE-1": ["CBE-2", "CBE-3"],
    "CBE-2": ["CBE-4"],
    "CBE-3": ["CBE-5"],
    "CBE-4": [],
    "CBE-5": []
}


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.append(current)

            for person in graph[current]:
                queue.append(person)

    return visited


# Testing

account1 = Account("Almaz", "1001", 1000)
account2 = Account("Dawit", "1002", 2000)
account3 = Account("Hanna", "1003", 500)

account1.deposit(300)
account1.withdraw(100)

registry = AccountRegistry()

registry.add(account1)
registry.add(account2)
registry.add(account3)


print("Search:")
print(registry.find_by_number("1002").owner)


print("\nLeaderboard:")

for account in registry.top_by_balance(2):
    print(account.owner, account.balance)


print("\nTransactions:")
print(registry.total_transactions("1001"))


print("\nBank Total:")
print(head_office.total_balance())


print("\nReachable from CBE-1:")
print(bfs(transfers, "CBE-1"))
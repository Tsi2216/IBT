from account import Account


account1 = Account("Tsion", "001", 500)
account2 = Account("Abel", "002", 1000)


account1.deposit(200)
account1.withdraw(100)

account2.deposit(300)
account2.withdraw(200)


account1.statement()
print()

account2.statement()
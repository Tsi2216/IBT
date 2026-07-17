from account import Account

account1 = Account("John", "1001", 500)
account2 = Account("Sara", "1002", 1000)

account1.deposit(200)
account1.withdraw(100)

account2.deposit(300)
account2.withdraw(2000)

account1.statement()
account2.statement()
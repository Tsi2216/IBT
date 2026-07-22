# 1. Book class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")


book1 = Book("Python Basics", "John", 250)
book2 = Book("Learning Git", "Mary", 180)

book1.describe()
book2.describe()


# 2. Product class

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        self.quantity -= n


product = Product("Rice", 200, 20)
product.restock(10)
product.sell(5)

print(product.quantity)


# 3. Make it private

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        self.__quantity -= n


# 4. Validate

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        if self.__quantity - n < 0:
            print("Quantity cannot go below zero.")
        else:
            self.__quantity -= n


# 5. Prove independence

product1 = Product("Milk", 80, 10)
product2 = Product("Bread", 40, 15)
product3 = Product("Sugar", 120, 20)

product1.sell(5)

print(product1.quantity)
print(product2.quantity)
print(product3.quantity)
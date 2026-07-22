# 1. Unique cities

cities = ["Addis Ababa", "Adama", "Addis Ababa", "Hawassa", "Adama"]

unique_cities = set(cities)

print(unique_cities)
print(len(unique_cities))


# 2. Price report

prices = {
    "Bread": 50,
    "Milk": 80,
    "Sugar": 120,
    "Rice": 200,
    "Oil": 350
}

for item, price in prices.items():
    print(item, price)


# 3. Tax comprehension

prices = [100, 250, 400, 80]

tax_prices = [price * 1.15 for price in prices]

print(tax_prices)


# 4. Cheap items

cheap_items = [price for price in prices if price < 200]

print(cheap_items)


# 5. Write & read

with open("names.txt", "w") as file:
    file.write("Almaz\n")
    file.write("Dawit\n")
    file.write("Tigist\n")

with open("names.txt", "r") as file:
    for name in file:
        print(name.strip())


# 6. Safe division

try:
    number = float(input("Enter a number: "))
    print(1000 / number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
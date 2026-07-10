# EXERCISE 1 - Temperature Label

temperature = int(input("Enter temperature (°C): "))

if temperature < 15:
    print("Cold")
elif temperature <= 28:
    print("Warm")
else:
    print("Hot")



# EXERCISE 2 - Receipt Loop


for i in range(1, 11):
    print(f"Receipt #{i}")



# EXERCISE 3 - Even Numbers


for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# EXERCISE 4 - Discount Function


def apply_discount(price, percent=10):
    return price - (price * percent / 100)

print(apply_discount(100))
print(apply_discount(100, 20))



# EXERCISE 5 - Countdown

count = 5

while count > 0:
    print(count)
    count -= 1

print("Liftoff!")
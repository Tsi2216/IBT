# 1. Temperature label

temperature = float(input("Enter temperature in °C: "))

if temperature < 15:
    print("cold")
elif temperature <= 28:
    print("warm")
else:
    print("hot")


# 2. Receipt loop

for i in range(1, 11):
    print(f"Receipt #{i}")


# 3. Even numbers

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 4. Discount function

def apply_discount(price, percent=10):
    return price - (price * percent / 100)

print(apply_discount(100))
print(apply_discount(100, 20))


# 5. Countdown

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Liftoff!")
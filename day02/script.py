# DAY 02 - PYTHON FUNDAMENTALS
# PART 1 - VARIABLES

student_name = "John Doe"      # String
age = 20                       # Integer
balance = 1500.50              # Float
is_enrolled = True             # Boolean
verified = None                # NoneType

print(student_name)
print(age)
print(balance)
print(is_enrolled)
print(verified)



# DATA TYPES

print(type(student_name))
print(type(age))
print(type(balance))
print(type(is_enrolled))
print(type(verified))


# VARIABLE NAMING RULES

student_name = "Sara"
student_age = 22
student_balance = 3500

# Correct
first_name = "John"

# Incorrect
# 1name = "John"
# first name = "John"
# for = 10


# USER INPUT

name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: {salary}")



# TYPE CONVERSION

number = "100"

print(int(number))
print(float(number))
print(str(500))



# ARITHMETIC OPERATORS

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Exponent:", a ** b)



# COMPARISON OPERATORS

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)



# LOGICAL OPERATORS

x = True
y = False

print(x and y)
print(x or y)
print(not x)


# IF, ELIF, ELSE

balance = 1500

if balance >= 1000:
    print("Premium Customer")
elif balance >= 500:
    print("Standard Customer")
else:
    print("Basic Customer")



# WHILE LOOP

count = 5

while count > 0:
    print(count)
    count -= 1

print("Finished")



# FOR LOOP WITH RANGE

for i in range(1, 6):
    print(i)


# RANGE EXAMPLES

print("range(5)")
for i in range(5):
    print(i)

print("range(1,5)")
for i in range(1, 5):
    print(i)

print("range(0,10,2)")
for i in range(0, 10, 2):
    print(i)


# BREAK

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# CONTINUE

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# LIST

students = ["John", "Sara", "Mike"]

print(students)

for student in students:
    print(student)



# FUNCTIONS

def greet(name):
    print(f"Hello {name}")


greet("John")
greet("Sara")



# FUNCTION WITH RETURN

def add(num1, num2):
    return num1 + num2


result = add(10, 20)
print(result)



# DEFAULT PARAMETERS

def add_tax(price, rate=0.15):
    return price + price * rate


print(add_tax(1000))
print(add_tax(1000, 0.10))



# KEYWORD ARGUMENTS

print(add_tax(price=5000, rate=0.20))



# VARIABLE SCOPE

tax_rate = 0.15


def total(price):
    fee = 50
    return price + fee


print(total(1000))
print(tax_rate)

# print(fee)
# NameError because fee is local.



# LOCAL VARIABLES


def student():
    name = "Abel"
    print(name)


student()


# GLOBAL VARIABLES


country = "Ethiopia"


def display_country():
    print(country)


display_country()


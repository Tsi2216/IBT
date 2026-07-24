# Question 1

def getOnlyEvens(numbers):
    result = []

    for index in range(len(numbers)):
        if index % 2 == 0 and numbers[index] % 2 == 0:
            result.append(numbers[index])

    print(result)


getOnlyEvens([1, 2, 3, 6, 4, 8])
getOnlyEvens([0, 1, 2, 3, 4])


# Question 2

def reverseCompare(number):
    first_digit = number // 10
    second_digit = number % 10

    reversed_number = second_digit * 10 + first_digit

    if number > reversed_number:
        print("Ok")
    else:
        print("Not ok")


reverseCompare(72)
reverseCompare(23)


# Question 3

def returnFactorial(number):
    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    return factorial


print(returnFactorial(5))
print(returnFactorial(6))
print(returnFactorial(0))


# Question 4

def checkMeera(numbers):
    for number in numbers:
        if number * 2 in numbers:
            print("I am NOT a Meera array")
            return

    print("I am a Meera array")


checkMeera([10, 4, 0, 5])
checkMeera([7, 4, 9])
checkMeera([1, -6, 4, -3])


# Question 5

def isDual(numbers):
    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    for count in counts.values():
        if count != 2:
            return 0

    return 1


print(isDual([1, 2, 1, 3, 3, 2]))
print(isDual([2, 5, 2, 5, 5]))
print(isDual([3, 1, 1, 2, 2]))


# Question 6

def digitalClock(seconds):
    seconds %= 86400

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))
total = 100
number_of_people = 5


def split_the_bill(total, number_of_people, rate=0.10):
    total_with_tip = total + (total * rate)
    return total_with_tip / number_of_people


print(split_the_bill(total, number_of_people))
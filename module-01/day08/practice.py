# 1. Recursive sum and countdown

def total(nums):
    if len(nums) == 0:
        return 0

    return nums[0] + total(nums[1:])


def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)


print(total([10, 20, 30]))

count_down(5)


# 2. Binary search

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


balances = [100, 300, 500, 800, 1000]

print(binary_search(balances, 800))


# 3. Merge sort

def merge(left, right):

    result = []

    while left and right:

        if left[0] <= right[0]:
            result.append(left.pop(0))

        else:
            result.append(right.pop(0))


    result.extend(left)
    result.extend(right)

    return result



def merge_sort(items):

    if len(items) <= 1:
        return items


    middle = len(items) // 2

    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])


    return merge(left, right)



numbers = [5, 2, 9, 1, 7]

print(merge_sort(numbers))


# 4. Sort with key

accounts = [
    ("Almaz", 1500),
    ("Dawit", 700),
    ("Hanna", 2000)
]


sorted_accounts = sorted(
    accounts,
    key=lambda account: account[1],
    reverse=True
)


print(sorted_accounts)



# 5. Two pointers


def has_pair(nums, target):

    left = 0
    right = len(nums) - 1


    while left < right:

        total = nums[left] + nums[right]


        if total == target:
            return True

        elif total < target:
            left += 1

        else:
            right -= 1


    return False



print(has_pair([1,2,3,4,5], 7))
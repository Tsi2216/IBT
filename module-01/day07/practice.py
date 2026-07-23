import time

accounts_list = [f"ACC{i}" for i in range(100000)]

accounts_dict = {
    f"ACC{i}": i for i in range(100000)
}

target = "ACC99999"

start = time.time()
target in accounts_list
print("List lookup time:", time.time() - start)


start = time.time()
target in accounts_dict
print("Dict lookup time:", time.time() - start)


# 3. Build a stack

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


names = ["Almaz", "Dawit", "Hanna"]

stack = Stack()

for name in names:
    stack.push(name)

reversed_names = []

while stack.items:
    reversed_names.append(stack.pop())

print(reversed_names)


# 4. Build a queue

from collections import deque

bank_line = deque()

bank_line.append("Almaz")
bank_line.append("Dawit")
bank_line.append("Hanna")
bank_line.append("Samuel")
bank_line.append("Tigist")

while bank_line:
    print(bank_line.popleft())


# 5. Singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


linked_list = LinkedList()

linked_list.push_front("Almaz")
linked_list.push_front("Dawit")
linked_list.push_front("Hanna")

linked_list.print_all()
import heapq
from collections import deque


# 1. Build a BST

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):

    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root


def inorder(root):

    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


root = None

balances = [500, 1200, 300, 800, 2000]

for balance in balances:
    root = insert(root, balance)

print("BST In-order:")
inorder(root)


# 2. Tree depth

def height(node):

    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return max(left_height, right_height) + 1


print("Tree height:")
print(height(root))


# 3. Graph BFS

graph = {
    "1001": ["1002", "1003"],
    "1002": ["1004"],
    "1003": ["1005"],
    "1004": [],
    "1005": []
}


def bfs(graph, start):

    visited = set()
    queue = deque([start])

    while queue:

        current = queue.popleft()

        if current not in visited:

            visited.add(current)

            for neighbor in graph[current]:
                queue.append(neighbor)

    return visited


print("BFS:")
print(bfs(graph, "1001"))


# 4. Graph DFS

def dfs(graph, start, visited=None):

    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph[start]:

        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


print("DFS:")
print(dfs(graph, "1001"))


# 5. Priority queue

tasks = []

heapq.heappush(tasks, (3, "Check account"))
heapq.heappush(tasks, (1, "Deposit money"))
heapq.heappush(tasks, (5, "Print report"))
heapq.heappush(tasks, (2, "Withdraw money"))
heapq.heappush(tasks, (4, "Transfer money"))


print("Priority Queue:")

while tasks:

    print(heapq.heappop(tasks))
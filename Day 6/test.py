class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

head = Node(1)
_1 = Node(2)
head.next = _1
_2 = Node(3)
head.next.next = _2

second = head
second.next = _2
print(head.next.key)
print(second.next.key)
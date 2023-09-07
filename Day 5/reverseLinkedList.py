class Node():
    def __init__(self, k):
        self.key = k
        self.next = None

def revLinkedList(head):
    newHead = None
    while head != None:
        next = head.next
        head.next = newHead
        newHead = head
        head = next
    return newHead

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

head = Node(3)
head.next = Node(6)
head.next.next = Node(8)
head.next.next.next = Node(10)

head = revLinkedList(head)

printLinkedList(head)

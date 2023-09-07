class Node():
    def __init__(self, k):
        self.key = k
        self.next = None
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

head = Node(3)
head.next = Node(6)
head.next.next = Node(8)
head.next.next.next = Node(10)
# printLinkedList(head)        

def middle(head):
    curr = head
    count = 0
    while curr != None:
        count += 1
        curr = curr.next
    curr = head
    for i in range(count//2):
        curr = curr.next
    return curr.key

print(middle(head))
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

def middle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow.key

print(middle(head))
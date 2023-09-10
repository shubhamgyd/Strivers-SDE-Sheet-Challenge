class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

def delete(temp):
    temp.key = temp.next.key
    temp.next = temp.next.next
    
          
head = Node(1)
head.next = Node(4)
head.next.next = Node(2)
head.next.next.next = Node(3)

printLinkedList(head)
delete(head.next.next)
printLinkedList(head)
print()
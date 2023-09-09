class Node():
    def __init__(self, k):
        self.key = k
        self.next = None

def remove(head,pos):
    dummy = Node(None)
    dummy.next = head
    first = dummy
    second = dummy
    for i in range(pos):
        second = second.next
    while second.next != None:
        first = first.next
        second = second.next
    first.next = first.next.next
    return head

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head = remove(head, 3)
printLinkedList(head)



    
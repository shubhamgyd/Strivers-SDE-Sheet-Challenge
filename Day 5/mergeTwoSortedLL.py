# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def sortTwoLists(first, second):
    temp = Node(0)
    res = temp
    
    while first != None and second != None:
        if first.data < second.data:
            temp.next = first
            temp = temp.next
            first = first.next
        else:
            temp.next = second
            temp = temp.next
            second = second.next
    if first != None:
        temp.next = first
    else:
        temp.next = second
    
    return res.next

first = Node(1)
first.next = Node(4)
first.next.next = Node(5)
second = Node(2)
second.next = Node(3)
second.next.next = Node(5)

head = sortTwoLists(first, second)
printLinkedList(head)
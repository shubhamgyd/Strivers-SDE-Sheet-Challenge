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
    curr1 = first
    curr2 = second
    head = None
    if curr1.data < curr2.data:
        curr = curr1
        curr1 = curr1.next
    else:
        curr = curr2
        curr2 = curr2.next
    # print(curr.data)
    curr3 = Node(curr.data)
    head = curr3
    
    while (curr1 != None and curr2 != None):
        if curr1.data > curr2.data:
            temp = curr2
            # print(curr2.data)
            temp.next = head.next
            head.next = temp
            print(head.next.data)
            print(curr2.data)
            curr2 = curr2.next
            head = head.next
        else:
            temp = curr1
            print(temp.data)
            temp.next = head.next
            # print(head.data)
            head.next = temp
            curr1 = curr1.next
            print(head.next.data)
            print(temp.data) 
            head = head.next
    # printLinkedList(head)
    if curr1 != None:
        head.next = curr1
    elif curr2 != None:
        head.next = curr2
    return curr

first = Node(1)
first.next = Node(4)
first.next.next = Node(5)
second = Node(2)
second.next = Node(3)
second.next.next = Node(5)

head = sortTwoLists(first, second)
printLinkedList(head)
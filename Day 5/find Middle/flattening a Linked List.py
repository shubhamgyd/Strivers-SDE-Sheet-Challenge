class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.bottom


def mergeTwoLists(a, b):
    temp = Node(0)
    res = temp
    while a != None and b != None:
        if a.data < b.data:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
    if a:
        temp.bottom = a
    else:
        temp.bottom = b
    return res.bottom




def flatten(root):
    if root == None or root.next == None:
        return root
    # recur for list on right
    root.next = flatten(root.next)


    # now merge
    root = mergeTwoLists(root, root.next)


    # return the root
    # it will be in turn merged with its left
    return root

l1 = Node(5)
l1.bottom = Node(7)
l1.bottom.bottom = Node(8)
l1.bottom.bottom.bottom = Node(10)
l2 = Node(10)
l2.bottom = Node(20)
l3 = Node(19)
l3.bottom = Node(22)
l3.bottom.bottom = Node(50)
l4 = Node(28)
l4.bottom = Node(35)
l4.bottom.bottom = Node(40)
l4.bottom.bottom.bottom = Node(45)
l1.next = l2
l2.next = l3
l3.next = l4

head = flatten(l1)
printLinkedList(head)
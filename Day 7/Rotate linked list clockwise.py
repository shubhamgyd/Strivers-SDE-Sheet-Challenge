class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to rotate list by k times
def rotateRight(head, k):
    if head == None or head.next == None:
        return head
    for i in range(k):
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp1 = temp.next
        temp.next = None
        temp1.next = head
        head = temp1
    return temp1
        
        




# utility function to print list
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)
    return




if __name__ == '__main__':
    head = None
    # inserting Node
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)


    print("Original list: ", end='')
    printList(head)


    k = 2
    # calling function for rotating right of the nodes by k times
    newHead = rotateRight(head, k)


    print("After", k, "iterations: ", end='')
    printList(newHead)  # list after rotating nodes
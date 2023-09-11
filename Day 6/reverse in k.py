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




# utility function to find length of the linked list
def lengthOfLinkedList(head):
    length = 0
    while head != None:
        length += 1
        head = head.next
    return length




# utility function to reverse k nodes in the linked list
def reverseKNodes(head, k):
    if head == None or head.next == None:
        return head


    length = lengthOfLinkedList(head)


    dummyHead = Node(0)
    dummyHead.next = head


    pre = dummyHead
    cur = None
    nex = None


    while length >= k:
        cur = pre.next
        nex = cur.next
        for i in range(1, k):
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        pre = cur
        length -= k
    return dummyHead.next




# utility function to print the linked list
def printLinkedList(head):
    while head.next != None:
        print(head.val, end="->")
        head = head.next
    print(head.val)




if __name__ == "__main__":
    head = None
    k = 3
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)
    head = insertNode(head, 6)
    head = insertNode(head, 7)
    head = insertNode(head, 8)


    print("Original Linked List: ", end="")
    printLinkedList(head)
    print("After Reversal of k nodes: ", end="")
    newHead = reverseKNodes(head, k)
    printLinkedList(newHead)
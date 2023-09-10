class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

def addTwoNumbers(l1, l2):
    dummy = Node(0)
    temp = dummy
    carry = 0
    while (l1 != None or l2 != None or carry):
        sum = 0
        if l1 != None:
            sum += l1.key
            l1 = l1.next
        if l2 != None:
            sum += l2.key
            l2 = l2.next
        sum += carry
        carry = sum // 10
        node = Node(sum%10)
        temp.next = node
        temp = temp.next
    return dummy.next

first = Node(1)
first.next = Node(4)
first.next.next = Node(5)
second = Node(2)
second.next = Node(3)
second.next.next = Node(5)

head = addTwoNumbers(first, second)
printLinkedList(head)
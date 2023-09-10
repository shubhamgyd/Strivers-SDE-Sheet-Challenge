class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

# inserting at the end of the linked list
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

def getDifference(head1, head2):
    len1 = 0
    len2 = 0
    while head1 != None or head2 != None:
        if head1 != None:
            len1 += 1
            head1 = head1.next
        if head2 != None:
            len2 += 1
            head2 = head2.next
    # if difference is neg-> length of list2 > length of list1 else vice-versa
    return len1 - len2

# utility function to check presence of intersection
def intersection(head1, head2):
    diff = getDifference(head1, head2)
    if diff < 0:
        while diff != 0:
            head2 = head2.next
            diff += 1
    else:
        while diff != 0:
            head1 = head1.next
            diff -= 1
    while head1 != None:
        if head1 == head2:
            return head1
        head2 = head2.next
        head1 = head1.next
    return head1

# utility function to print linked list created
def printList(head):
    while head.next != None:
        print(head.key, end="->")
        head = head.next
    print(head.key)
    
    
if __name__=="__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersection(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.key)

# Time Complexity: O(2max(length 0f list1, length of list2)) + O(abs(length of list1 -length of list2)) + O(min(length of list1, length of list2))
# Space Complexity: O(1 )
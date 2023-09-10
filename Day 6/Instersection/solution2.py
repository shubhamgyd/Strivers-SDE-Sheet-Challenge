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

# utility function to check presence of intersection
def intersection(head1, head2):
    st = set()
    while head1 != None:
        st.add(head1)
        head1 = head1.next
    while head2 != None:
        if head2 in st:
            return head2
        head2 = head2.next
    return None


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

# Time Complexity: O(n + m)
# Space Complexity: O(n)
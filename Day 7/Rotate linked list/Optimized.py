# https://takeuforward.org/data-structure/rotate-a-linked-list/
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
    curr = head
    length = 1
    while curr.next != None:
        curr = curr.next
        length += 1
    curr.next = head
    if k > length:
        length = k % length
    iterations = length - k
    while iterations:
        curr = curr.next
        iterations -= 1
    head = curr.next
    curr.next = None
    return head


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
    
# Time Complexity: O(Length of linked List) + O(Length of linked list - (k % linked list))
# Space Complexity: O(1)

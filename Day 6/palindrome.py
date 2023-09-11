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




def reverse(ptr):
    pre = None
    nex = None
    while ptr != None:
        nex = ptr.next
        ptr.next = pre
        pre = ptr
        ptr = nex
    return pre




def isPalindrome(head):
    if head == None or head.next == None:
        return True
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    slow.next = reverse(slow.next)
    slow = slow.next
    dummy = head
    while slow != None:
        if dummy.val != slow.val:
            return False
        dummy = dummy.next
        slow = slow.next
    return True




if __name__ == "__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 2)
    head = insertNode(head, 1)
    print(isPalindrome(head))
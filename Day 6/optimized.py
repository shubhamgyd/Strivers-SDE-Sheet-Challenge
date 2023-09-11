class Node:
    def __init__(self, k):
        self.key = k
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

# utility function to create cycle
def createCycle(head, pos):
    temp = head
    ptr = head
    cnt = 0
    while temp.next != None:
        if cnt != pos:
            ptr = ptr.next
            cnt += 1
        temp = temp.next
    temp.next = ptr
    
# process as per mentioned in solution
def detectCycle(head):
    if head == None or head.next == None:
        return None
    fast = head
    slow = head
    entry = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return slow
    return None

if __name__=="__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 3)
    head = insertNode(head, 6)
    head = insertNode(head, 10)
    createCycle(head, 2)
    nodeRecieve = detectCycle(head)
    if nodeRecieve == None:
        print("No cycle")
    else:
        temp = head
        pos = 0
        while temp != nodeRecieve:
            pos += 1
            temp = temp.next
        print("Tail connects at pos", pos)
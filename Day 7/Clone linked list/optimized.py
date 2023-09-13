class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        self.random = None

def deepcopy(head):
    temp = head
    while temp != None:
        temp1 = Node(temp.key)
        temp1.next = temp.next
        temp.next = temp1
        temp = temp.next.next
    
    itr = head
    while itr != None:
        if(itr.random != None):
            itr.next.random = itr.random.next
        itr = itr.next.next

    itr = head
    dummy = Node(0)
    temp = dummy
    while itr != None:
        fast = itr.next.next
        temp.next = itr.next
        itr.next = fast
        temp = temp.next
        itr = fast

    return dummy.next

def printList(head):
    while head != None:
        print(head.key)
        print(head.next.key) if head.next != None else None
        print(head.random.key) if head.random != None else None
        print()
        head = head.next
        
if __name__=="__main__":
    head = None
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    head = node1
    head.next = node2
    head.next.next = node3
    head.next.next.next = node4
    
    head.random = node4
    head.next.random = node1
    head.next.next.random = None
    head.next.next.next.random = node2
    
    print("Original list: (current node:node pointed by next pointer, node pointed by random pointer)\n")
    printList(head);
    
    print("Copy list:(current node:node pointed by next pointer, node pointed by random pointer)\n")
    newHead = deepcopy(head)
    printList(newHead)
    
# Time Complexity: O(N) + O(N)

# Reason: Two iterations over the entire list. Once for inserting in the map and other for linking
# nodes with next and random pointer.

# Space Complexity: O(N)

# Reason: Use of hashmap for storing entire data.
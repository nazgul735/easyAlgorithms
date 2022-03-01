
class LinkedList:
    def __init__(self, *args, **kwargs):
        self.head = self.Node(None)
    class Node:
        def __init__(self, data):
            self.data=data
            self.next=None
    def push(self, data):
        node = self.Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        node = self.head
        while node.next is not None:
            print(node.data, end = " ")
            node = node.next
     
    # count number of node in linked list
    def countNodes(self):
        count = 0
        node = self.head
        while node.next is not None:
            count += 1
            node = node.next
        return count
    
    def swapKth(self, k):
 
        # Count nodes in linked list
        n = self.countNodes()
 
        # check if k is valid
        if n<k:
            return
        if (2 * k - 1) == n:
            return
        x = self.head
        x_prev = self.Node(None)
        for i in range(k - 1):
            x_prev = x
            x = x.next
        y = self.head
        y_prev = self.Node(None)
        for i in range(n - k):
            y_prev = y
            y = y.next
        if x_prev is not None:
            x_prev.next = y
 
        # Same thing applies to y_prev
        if y_prev is not None:
            y_prev.next = x
         
        temp = x.next
        x.next = y.next
        y.next = temp
 
        # Change head pointers when k is 1 or n
        if k == 1:
            self.head = y
         
        if k == n:
            self.head = x
 
# Driver Code
llist = LinkedList()
for i in range(8, 0, -1):
    llist.push(i)
llist.printList()
 
 
for i in range(1, 9):
    llist.swapKth(i)
    print("Modified List for k = ", i)
    llist.printList()
    print("\n")
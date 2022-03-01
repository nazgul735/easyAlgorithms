class Solution(object):
    def __init__(self):
        self.head=None
    class Node:
        def __init__(self, data):
            self.data=data
            self.next=None
    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printNthNode(self, n):
        current=self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
         
        # print count
        if n > length: 
                       
            print('Location is greater than the' +
                         ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)

class LinkedList(object):
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
    def printList(self):
        temp=self.head
        while temp is not None:
            print(str(temp.data), end=" ")
            temp=temp.next
    def betterSort(self):
        temp,ptr={},self.head
        while ptr is not None:
            temp[ptr.data]=1 if ptr.data not in temp else temp[ptr.data]+1
            ptr=ptr.next
        sortedTemp=sorted(temp.items(), key=lambda item: item[0])
        ptr=self.head
        for i in sortedTemp: 
            for j in range(i[1]):
                ptr.data=i[0]
                ptr=ptr.next
            


llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(1)
llist.push(1)
llist.push(1)
llist.push(3)
 
print ("Linked List before sorting")
llist.printList()
print("\n --------------------")
llist.betterSort()
llist.printList()
print("\n --------------------")

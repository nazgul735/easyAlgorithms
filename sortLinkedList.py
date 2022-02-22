from collections import defaultdict
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
    # def sortList(self):
    #     count=[0,0,0]
    #     current=self.head
    #     while current != None:
    #         count[current.data]+=1
    #         current=current.next
    #     i=0
    #     current=self.head
    #     while current != None:
    #         if count[i]==0:
    #             i+=1
    #         else:
    #             current.data=i
    #             count[i]-=1
    #             current=current.next
    def betterSort(self):
        temp,ptr={},self.head
        while ptr is not None:
            temp[ptr.data]=1 if ptr.data not in temp else temp[ptr.data]+1
            ptr=ptr.next
        sortedTemp=sorted(temp.items(), key=lambda item: item[0])
        ptr=self.head
        #  ptr.data, ptr=i[0], ptr.next for i, j in itertools.product(sortedTemp, range(i[1])):
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
 
print ("Linked List before sorting")
print("\n --------------------")
llist.betterSort()
llist.printList()
print("\n --------------------")

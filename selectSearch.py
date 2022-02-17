some_list=[8,7,2,3,4,5]
def selectSort(unsortedlist):
    print(unsortedlist)
    for i in range(len(unsortedlist)):
        smallestNumber=i
        for j in range(i + 1, len(unsortedlist)):
            if unsortedlist[j] < unsortedlist[smallestNumber]:
                smallestNumber=j
        unsortedlist[smallestNumber], unsortedlist[i]=unsortedlist[i], unsortedlist[smallestNumber]
    print(unsortedlist)

print(selectSort(some_list))


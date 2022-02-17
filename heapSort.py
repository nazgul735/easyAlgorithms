def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
 
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap. Goes from middle and down Range(start, end, step)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
 
 
# Driver code
arr = [4, 10, 3, 5, 1]
heapSort(arr)
n = len(arr)

for i in range(n):
    print("%d" % arr[i],end=" ")
    
# O(Logn)=x --> 2^x=n

# Input data: 4, 10, 3, 5, 1
#          4(0)
#         /   \
#      10(1)   3(2)
#     /   \
#  5(3)    1(4)
# string ="abcg"
# n = [ord(x) - 96 for x in string]


def sort012(arr, n):

    l=0
    h=n-1
    mid=0

    while mid<=h:
        if arr[mid]==0:
            arr[l], arr[mid]=arr[mid], arr[l]
            l=l+1
            mid=mid+1
        elif arr[mid]==1:
            mid= mid+1
        else:
            arr[mid], arr[h]=arr[h], arr[mid]
            h=h-1
    return arr

def printArr( a):
    for j in a:
        print(j, end=' ')

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n=len( arr)
arr=sort012( arr, n)
printArr(arr)
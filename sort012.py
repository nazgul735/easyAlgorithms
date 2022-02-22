# string ="abcg"
# n = [ord(x) - 96 for x in string]
def sort012(arr, n):
    l = 0
    r=n-1
    mid=r//2
    sortedArr=[]
    for i in range(n):
        if arr[i]==0:
            sortedArr.insert(l, arr[i])
        elif arr[i]==1:
            sortedArr.insert(mid, arr[i])
        else:
            sortedArr.insert(r, arr[i])
    return sortedArr
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n=len(arr)
print(sort012(arr, n))


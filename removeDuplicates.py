def removeDupl(arr, n):
    if n<=1:
        return n
    temp=[arr[0]]
    for i in range(1, n):
        if arr[i] not in temp:
            temp.append(arr[i])
    string=f"Size of new array: {len(temp)}"
    return sorted(temp), string
def improved(arr, n):
    return n if n<=1 else dict()
arr=[1,1,2,2,4,5,6,21,1,7,100,110]
print(improved(arr, len(arr)))


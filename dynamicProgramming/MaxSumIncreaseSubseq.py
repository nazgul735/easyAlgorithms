def maxSumIS(arr, n):
    max = 0
    msis = [arr[i] for i in range(n)]
    # Compute maximum sum
    # values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if(arr[i] > arr[j] and 
                msis[i] < msis[j] + arr[i]):
                msis[i] = msis[j] + arr[i]
 
    # Pick maximum of
    # all msis values
    for i in range(n):
        if max < msis[i]:
            max = msis[i]
    return max
 
# Driver Code
arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print(str(maxSumIS(arr, n)))
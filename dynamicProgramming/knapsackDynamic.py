def ks(W, weight, val, n):
    if n==0 or W==0:
        return 0
    if (weight[n-1] > W):
        return ks(W, weight, val, n-1)
    else:
        return max(val[n-1] + ks(W-weight[n-1], weight, val, n-1), ks(W, weight, val, n-1))
 
 
#Driver Code
val = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(val)
print (ks(W, weight, val, n))
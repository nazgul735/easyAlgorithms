from cgi import print_directory


def distinctIds(arr, mi):
    n = len(arr)
    m = {}
    v = []
    count = 0
    
    # Store the occurrence of ids
    for i in range(n):
        if arr[i] in m:
            m[arr[i]] += 1

        else:
            m[arr[i]] = 1



   
    # Store into the list value as key and vice-versa
    for i in m:
        v.append([m[i],i]) #value=i and m[i]=key --> sort will set value first
    v.sort()
    size = len(v)


    # Start removing elements from the beginning
    for i in range(size):
    # Remove if current value is less than
    # or equal to mi
        if (v[i][0] <= mi):
            mi -= v[i][0]
            count += 1


        else:   # Return the remaining size
            return size - count
    return size - count
    
    

# Driver code
arr = [2, 3, 1, 2, 3, 3, 1, 1 ]

mi = 3

# To display the result
print(distinctIds(arr, mi))

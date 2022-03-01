def partition(start, end, array):

    pivot_index = start
    pivot = array[pivot_index]
    
    while start < end:
    
        while start < len(array) and array[start] <= pivot:
            start += 1
    
        while array[end] > pivot:
            
            end -= 1
    
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    return end

def quick_sort(start, end, array):
    
    if (start < end):
    
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

def printMedian(arr, n):
    quick_sort(0, n-1, arr)
    print(arr)

    return (arr[n//2-1]/2.0+arr[n//2]/2.0, arr[n//2])[n % 2] if n else None

arr=[5, 15, 1, 3, 2, 8, 7, 10, 14]
n=len(arr)
print(printMedian(arr, n))


    

        
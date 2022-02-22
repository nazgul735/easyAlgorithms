def mergeSort(list):
    #string="hei"
    #list = [ord(x) - 96 for x in string] 
    if len(list) > 1:

        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
       
        mergeSort(left)
        mergeSort(right)

        k=0
        i=0
        j=0
        
        while i < len(left) and j < len(right):
            if left[i]<=right[j]:
                list[k]= left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
             
        while i<len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1
list=[4,5,6,0,1,4,5,10]
mergeSort(list)
print(list)



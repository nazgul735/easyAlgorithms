import numpy as np
def medianOf2Arr(arr1,arr2):
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    temp=np.concatenate((arr1,arr2))
    temp1=np.hstack([arr1, arr2])
    return temp

arr1,arr2=[],[]
print(medianOf2Arr(arr1,arr2))
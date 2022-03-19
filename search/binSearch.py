some_list=[8,7,2,3,4,5]

def binSearch(list, num, left_side, right_side):
    left_side, right_side=0, len(list)-1
    if left_side<=right_side:
        middle = left_side + (right_side-1)//2
        if list[middle]==num:
            return middle
        elif list[middle]<num:
            return binSearch(list, num, middle+1, right_side)
        else:
            return binSearch(list, num, left_side, middle-1)
    return -1
print(binSearch(some_list, 3))
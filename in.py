def solution(list):
    list1=list
    for i, j in zip(list, list1[1:]):
        if i<j:
            continue
        else:
            return False
    return True




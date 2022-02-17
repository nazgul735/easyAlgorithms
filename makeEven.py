import sys

from black import main

def evenNum(arr, n):
    #index
    firstEvnNum=-1
    lastEvnNum=-1
    lastNum=n-1

    for i in range(n):
        if(int(arr[i])%2==0 and int(arr[i])<int(arr[lastEvnNum])):
            firstEvnNum=i
            break
        elif int(arr[i]) % 2 == 0:
            lastEvnNum = i

    if firstEvnNum != -1:
        (arr[firstEvnNum],arr[lastNum]) = (arr[lastNum],arr[firstEvnNum])
        return arr

    if firstEvnNum == -1 and lastEvnNum != -1:
         
        # swap even and odd value
        (arr[lastEvnNum],
         arr[lastNum]) = (arr[lastNum],
                           arr[lastEvnNum])
        return arr
    return arr
if __name__=='__main__':
    string="1356425"
    result = "".join(evenNum(list(string),len(list(string))))
    print(result)


    
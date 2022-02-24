def onlyAlpha(string):
    dict={}
    i=0
    stack=string.split(" ")
    for woird in range(len(stack)): 
        i+=1
        print(i)
        if any(char.isdigit() for char in stack[i]):
            print(stack[i])
            stack.remove(stack[i])  

    print(stack)

string="hei din hore hei hei123 hei2"
onlyAlpha(string)
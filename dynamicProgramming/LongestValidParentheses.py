def longestValidParentheses(self, s):
    l,r,max_ = 0,0,0
    for i in range(len(s)):
        if s[i] == '(':
            l +=1
        else:
            r +=1
        if l == r:
            max_ = max(max_, 2 * r)
        else:
            if r >= l:
                l = r = 0
    l,r = 0,0
    for i in range(len(s)-1,-1,-1):
        if s[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            max_ = max(max_, 2 * l)
        else:
            if l >= r:
                l = r = 0
    return max_

def sortingProperly(self,s):
    l,r=0,0
    mid=len(s)//2
    for i, j in zip(range(len(s)), range(len(s)-1,-1,-1)):
        l=l+2 if s[i] == '(' and s[j]=='(' else l
        l =l+1 if s[i] == '(' or s[j]=='(' and s[j]!=s[i] else l
        r=r+2 if s[i] == ')' and s[j]==')' else r
        r=r+1 if s[i] == ')' or s[j]==')' and s[j]!=s[i] else r
    l,r=l//2,r//2
    return int((min(l,r)))*("("+")"), len(int((min(l,r))/2)*("("+")"))*2     
def binSort(self, s):
    d={"(":0,")":0}
    mid=len(s)//2; left=s[:mid]; right=s[mid:]
    for i, j in zip(range(len(left)), range(len(right))):
        d["("]+=2 if left[i] == '(' and right[j]=='(' else next
        d["("]+=1 if left[i] == '(' or right[j]=='(' and right[j]!=left[i] else next
        d[")"]+=2 if left[i] == ')' and right[j]==')' else next
        d[")"]+=1 if left[i] == ')' or right[j]==')' and right[j]!=left[i] else next
    return min(d.values())*("()")   
def betterBinSort(self, s): #unsure about this 
    d={"(":0,")":0}
    mid=len(s)//2; left=s[:mid]; right=s[mid:]
    for i, j in zip(range(len(left)), range(len(right))):
        d[left[i]]+=1 if (left[i], right[j]) in d else 1
        d[right[j]]+=1 if right[j] in d else 1
    return min(d.values())*2
def patSort(self, s):
    n = len(s)
    stack = []
    longest = [0]*n
    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        elif stack:
            start = stack.pop()
            longest[i] = i - start + 1
            if start > 0:
                longest[i] += longest[start - 1]
    return max(longest or [0]) 

string="()()()"
# print(patSort(0, string))

print(betterBinSort(0, string))


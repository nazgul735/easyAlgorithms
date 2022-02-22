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
    for i, j in zip(range(len(s)), range(len(s)-1,-1,-1)):
        l=l+2 if s[i] == '(' and s[j]=='(' else l
        l =l+1 if s[i] == '(' or s[j]=='(' and s[j]!=s[i] else l
        r=r+2 if s[i] == ')' and s[j]==')' else r
        r=r+1 if s[i] == ')' or s[j]==')' and s[j]!=s[i] else r
    l,r=l//2,r//2
    return int((min(l,r)))*("("+")"), len(int((min(l,r))/2)*("("+")"))*2            

string="()()()()(()))"
print("original lengde", len(string))
print(sortingProperly(0, string))
print(longestValidParentheses(0, string))


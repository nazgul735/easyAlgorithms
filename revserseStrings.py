def revserseWords(string, l, r):
    while l<r:
        string[l], string[r]=string[l], string[r]
        l, r = l+1, r-1

string = "i like this program very much"
l, r=0, len(string)-1
s = list(string)
s.reverse()
s = "".join(s)
print(s)
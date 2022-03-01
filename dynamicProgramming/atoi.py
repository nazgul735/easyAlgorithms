def atoi(string):
    res=0
    for i in range(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))
        print(res)
    return res

string="123456"
print(atoi(string))
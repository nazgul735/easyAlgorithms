def solution1(st):
    dict = {}
    st=st.replace(" ", "").lower()

    for s in st:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    items = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    string = ""
    string1=""
    for item in items:
        #if only 1 we want alphabetical arrangement
        if item[1]==1:
            string1=string1+item[0]
        #if more than 1 we want increase frequency
        if item[1] > 1:
            string = string + item[0]*item[1]
    sorted_characters = sorted(string1)
    string1="".join(sorted_characters)
    return string+string1

print(solution1("hanneAAAAe renho re"))
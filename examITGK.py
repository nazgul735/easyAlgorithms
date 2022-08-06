import random
import string
def solution():
    letters=""
    numbers=""
    for i in range(2):
            letters=letters+(str(random.choice(string.ascii_letters))).upper()
    for j in range(5):
        if j==1:
            numbers=numbers+str(random.randint(1, 9))
        else:
            numbers=numbers+str(random.randint(0, 9))
    return letters+numbers
print(solution())
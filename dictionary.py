try:
    from itertools import zip
except ImportError:
    pass
def dict1(dict):
    for i, v in zip(range(0,100), range(0,200,2)): dict[i]=str(v)
    print(dict)
dict={}
dict1(dict)

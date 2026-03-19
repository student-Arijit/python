import math

def mymap(func, it):
    for item in it:
        yield func(item)

nums = [5, -3, 10, -8, 0, 2]
m = list(mymap(lambda x: math.sqrt(x), filter(lambda x: x>=0, nums)))
print(m)

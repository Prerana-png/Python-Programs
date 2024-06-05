a=12
b=24
def min(a, b):
 if a <= b:
    return a
 else:
    return b

print(min(a,b))

#using min
minimum = min(a, b)
print(minimum)

#using sorted
print(sorted([a,b])[0])

#using reduce
from functools import reduce
mini=reduce(lambda a,b:a if a<=b else b , [a, b])
print(mini)
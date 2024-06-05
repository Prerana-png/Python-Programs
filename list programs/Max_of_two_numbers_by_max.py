a=12
b=4

#using maximum
maximum=max(a,b)
print(maximum)

#ternary operator
print(a if a>=b else b )

#using lamba function
maxi= lambda a,b: a if a>=b else b
print(f'{maxi(a,b)} is a maximum number')

#using list comprehension
x=[a if a>=b else b]
print(x)

#by sorting
y=[a,b]
y.sort()
print(y[-1])

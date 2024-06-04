list=[1,2,3,4,5,6]

length= sum(1 for i in list)
len=sum(1 for _ in list)

print("The length of the list using sum is" , length)
print("The length of the list using comprehension is " , len)
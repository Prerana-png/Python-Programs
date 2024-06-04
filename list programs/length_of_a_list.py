from operator import length_hint

test_list = [1,2,3,4,5]
n=len(test_list)
m=length_hint(test_list)


print("The length of the list using list is " , n)
print("The length of the list using length_hint is" , m)
list1=[1,2,3,4,5,6,7]
i= 3
if i in list1:
    print("exists")
else:
    print("does not exist")

#using loop
for i in list1:
    if(i==4):
        print("exists")

#using count
count=list1.count(5)
if count>0:
    print("exists")
else:
    print("does not exist")


#using find method
test_list= list(map(str,list1))
y="-".join(test_list)

if y.find("15") != -1:
    print("exists")
else:
    print("not exists")

#using counter function
from collections import Counter
frequency=Counter(list1)
if(frequency[5])>0:
    print("exists")
else:
    print("does not exist")


#filter function
element_to_check=3
filtered_element=filter(lambda x: x == element_to_check, list1)
if list(filtered_element):
    print("exists")
else:
    print("does not exist")
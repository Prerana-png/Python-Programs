def swaplist(newlist):

    start , *middle , end = newlist
    newlist =[end , *middle , start]
    return newlist

newlist = [1,2,3,4,5]
print(swaplist(newlist))
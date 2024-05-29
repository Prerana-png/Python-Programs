def swaplist(newlist):

    first=newlist.pop(0)
    last=newlist.pop(-1)

    newlist.insert(0,last)
    newlist.append(first)

    return newlist

newlist = [1,2,3,4,5,6]
print(swaplist(newlist))
def swapPositions(list , pos1 , pos2):

    list[pos1] , list[pos2]=list[pos2] , list[pos1]
    return list

list=[21,22,23,24]
pos1 , pos2= 1, 3

print(swapPositions(list,pos1-1,pos2-1))
test_list =  [ 'Gfg' , 'is', 'best' , 'for' ,'Geeks']

print("The originial list is " + str(test_list))

res = [sub.replace('G','-').replace('e', 'G').replace('-', 'e') for sub in test_list]

print("The modified test list is " + str(res))
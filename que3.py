#Q3.Generate a new set with all items from both sets by removing numbers which are in both sets.
set1 = {10, 20, 30, 40, 50,25}
set2 = {30, 40, 50, 60, 70,100}

set3=set1.symmetric_difference(set2)
print(set3)

'''set3=set1^set2
print(set3)'''
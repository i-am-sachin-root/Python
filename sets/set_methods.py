"""
set.intersection() :- find the same elements in the set 
set1 = set1.difference(set2) :- compare one with other and find diff in one 
set.union :- add all sets together
"""

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8}

set1 = set1.intersection(set2) # finding same values in sets by using intersecion()
print("Common elements usng intersection() :", set1)

#find diff in set 1 with compared to set 2

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8}
set1 = set1.difference(set2) # if interchange then it will give 7,8
print("diff compared to set2 in set1 :",set1)

# add diff set in one with union 
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8}
set1 = set1.union(set2)
print("Adding both sets with union() method :", set1)


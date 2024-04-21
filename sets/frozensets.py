"""
Frozen sets are immutable, we cannot edit frozenset 
but we can take them and work for diff output line using intersection(),difference(),union()
"""

fset1 = {1,2,3,4}
fset2 = {3,4,7}

fset1 = frozenset(fset1)
fset2 = frozenset(fset2)

print("checking type of set :", type(fset1))

#fset1 = fset1.remove(2)
#print("Trying to remove frozensets element :",fset1) here we are removing frozenset element but we cannot 

#using intersection on sets 
fset1 = fset1.intersection(fset2)
print("intersection", fset1)

#using difference 
fset1 = {1,2,3,4}
fset2 = {3,4,7}
fset1 = fset1.difference(fset2) # checking difference in fset1 compared to fset2 
print("Differece :",fset1)

#using union 
fset1 = fset1.union(fset2)
print("union :",fset1)


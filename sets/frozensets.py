"""
Frozen sets are immutable 
"""

list1 = {1,2,3,4}
list2 = {3,4,7}

list1 = frozenset(list1)
list2 = frozenset(list2)

print("checking type of set :", type(list1))
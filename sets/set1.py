"""
Mathod 1 for set creation
set1 =  [1,2,3,4,5]
set1 = set(set1) :- using function to create set

Methid 2 for set creation 
set1 = {1,2,3,4,5}

imp :- we cannot repeate values in set 
"""

#Creating set using set()
set1 =  [1,2,3,4,5,5]
set1 = set(set1) # here we have to assign itself to get set otherwise it will be a list 
print(set1)


#creating set using {}
set2 = {12,13,13,14,15}
print("creating set using { } ", set2)

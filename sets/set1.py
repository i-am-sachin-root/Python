"""
Sets are mutable

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

#checking if element is in set or not 
print("Set1 elements :",set1)
print("Finding element using 'int' op :", 4 in set1)
print("If element is not available :", 20 in set1)


# adding values in the set
print("before :",set1)
#extra = {34,45,23,55}
#set1.extend(34,45,23,55)
set1.add(34) #it will add only 1 element 
print("Added new elements in set1 :", set1)

# remove element from  set 
print("Before removing element :", set1)
set1.remove(34)
print("after remving set :",set1)
"""
min(list) :- gives minimum values from the list 
max(list) :- gives max value from the list 
list1.append(x,z,z) :- we can add values in the end of the list 
List1.extend(x,y,z) :- extending another list on the list
del list1[id] :- deleting element from the list 
list1.pop(id) :- Taking specific value fro  list
"""

List1 = ["cisco", "google", 2900,14.0]
List2 = [1,2,43,-3,0]

print("min() will give min value from the list :",min(List2)) #find minimum value from the list
print("max() will give max value from list :", max(List2)) # finding max value from the list 

#Appending int the list 
exstra_list = ["Iron man","Bat man","Spider man"]
List1.append(exstra_list)
print("Appending values at the end of the list :",List1)  #This will add extra list inside the existing list 

#Extending the list 
ext_list = ["red", "blue", "yellow"]
List1.extend(ext_list)
print("extending list using extend() :",List1)

#Deleting element
del List1[1] 
print("Delet  element from list :", List1)

#Taking specific value fro  list
print("using pop to take specific element :", List1.pop(0))

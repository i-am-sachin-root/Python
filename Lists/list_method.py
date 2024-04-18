"""
min(list) :- gives minimum values from the list 
max(list) :- gives max value from the list 
list1.append(x,z,z) :- we can add values in the end of the list 
"""

List1 = ["cisco", "google", 2900,14.0]
List2 = [1,2,43,-3,0]

print("min() will give min value from the list :",min(List2)) #find minimum value from the list
print("max() will give max value from list :", max(List2)) # finding max value from the list 

#Appending int the list 
exstra_list = ["Iron man","Bat man","Spider man"]
List1.append(exstra_list)
print("Appending values at the end of the list :",List1)  #This will add extra list inside the existing list 
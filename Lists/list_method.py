"""
min(list) :- gives minimum values from the list 
max(list) :- gives max value from the list 
list1.append(x,z,z) :- we can add values in the end of the list 
List1.extend(x,y,z) :- extending another list on the list
del list1[id] :- deleting element from the list 
list1.pop(id) :- Taking specific value fro  list, removes from previous list
list1.remove() :- 
list1.insert(id, elemet) :- insert element in specified index of list 
list1.sort():- sorts the elements by asc or desc 
Methods like count(),append,(),index() also work on list 
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

#Taking specific value from  list it will also remove it from the list 
print("using pop to take specific element :", List1.pop(0))
print(List1)


# Removing element from list 
List2.remove(43)
print(List2)

#inserting element in the list 
print("Before :",List2)
lmath = len(List2); """ here we are using len()  to find the max length and will use this value as end value, and with this we'll be able to add at the end of the string.
                        """
List2.insert(lmath,"end of list")
print("inserting at the end of the list :",List2)

#sorting in the list 
print("Before sorting :", List2)
del List2[(lmath)] # deleting string because sorting will not happen in sttring and int list 
Lsort = List2 #creating variable to store the output of new list after deletion 
Lsort.sort() # sorting the new list 
print("After sorting:",Lsort)





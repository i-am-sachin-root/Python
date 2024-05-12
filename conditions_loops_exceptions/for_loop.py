"Used for iteration on the sequence "
list1 = ["Cisco","Juniper","Palo Alto","Fortinet"]
print("checking vcariable type",type(list1))


for i in list1: # here we perform the operation on the list elements one by one, one element taken in place of 'i' and inside block if perfomred
        #print(list1) # this will print the whole list 4 times
        print(i) # this will print elements one by one 

r = range(10)
for i in r:
        print("printing the range of r using for loop:",i)



list1 = ["Cisco","Fortinet","DELL","HP","google"]
for (index, element) in  enumerate(list1): # here we are printing the index as well as their elements 
        print(index,element)
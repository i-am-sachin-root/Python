"""List is mutable
   List = [] :- an empty list 
   List[x] = value :- change value in the list by its index no
   """

List1 = ["Cisco","2900/k9",2014,14.0] # added values in list some are string, float and int
print(List1)

print(len(List1)) #checking length of list 

print(List1[1]) #will give 1 no in the index 

#changing value in the string 
List1[2] = "ISR4321" 
print(List1)
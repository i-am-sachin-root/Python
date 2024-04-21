"""
- immutable list 
- it is ordered
- IMP :- used to keep data is sequence and unchangable 
- indexes and duplicates are allowed
- we cannot remove or add into tuples 
 """

#create single element tuple, normally tuple has many elements 
single_tuple = (1,)
print(type(single_tuple))
print("Creating tuple with single element just add ',' after element :",single_tuple)

#indexing is tuples 
tup1 = (1,2,3,4,5,6,6)
print("before :", tup1)
print("using single element using indexing :",tup1[3])

#variable to value assignment 
var1 = ("Cisco", "ISR4321", "14.2")  # here we are adding variables 
vendor, model, ios_version = var1  # here are our main category 
print(type(var1)) # checking types changed to tuple or still string 
print("Printing vaules from tuples :",vendor,model,ios_version)


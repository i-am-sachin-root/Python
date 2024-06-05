#creating for loop to find spr till 10
list1 = []
for i in range(10):
    result = i ** 2 
    list1.append(result)
print(list1)

# with list comprahenssion 
list2 = [x ** 2 for x in range(10)] #formula for x till 10 
print(list2)

#with if 
list3 = [x ** 2 for x in range(10) if x > 5]  #only will print 


#for set comprehenssion
set1 = {x ** 2 for x in range(10)}
"iterator is an object which traverse through a data stream one by one like list, tuple"

mylist = [1,2,3,4,5,6,7,8]

for i in mylist:
    print(i)

mylist2 = [1,2,3,4,5,6,7,8]
myiter = iter(mylist2) # creating iterator  they save computer resources that's why we use them 
print(next(myiter))


#generator 
"generator is a special routine that can be used to control the behaviour of the iteration loop"
"gnerator are also functions but they can be suspended and resumed as we want, normal function runs all the code "

def my_generator(x,y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y #yeild suspends the execution and sends value to the caller, also it saves the state of the execution

my_object = my_generator(10,5) #adding argument in the gnerator 

for z in my_object: #we can use next() here to get next value each time.
    print(next(my_object))

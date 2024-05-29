"""
1) Positional arguments:- no of arguments should same in finctions defination  and function parametrs 
def function(x,y) #this is parameters
    x y z #this is function definations 

2) Keyword argument:- we asign value to the parameter while calling.    
"""

# positional argument 
def funct1(x,y,z): #parameters 
    sum = (x + y) * z
    return sum
print(funct1(1,2,3)) #arguments

#keyword argument 
def funct2(x,y,z):
    sum = (x + y) * z
    return sum 
print(funct2(x=2,z=3,y=5)) # this is keyword argument 


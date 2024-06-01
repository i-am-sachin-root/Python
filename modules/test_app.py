import test_module  # type: ignore
# this is main code 
print("main code ")
print(test_module.var1) #here we are exctracting var1 from test_module.py

print(test_module.func1()) #using function from our test module 

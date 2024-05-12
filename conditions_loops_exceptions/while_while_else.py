""" while block executes the code block as long as the defined condition is true 
- if the condition stays true that means it will run infinatly 
- it will run as long as the condtions remains true, the moment conditions becomes false """

x = 1  # initilaization of the 1st value 

print("Printing the range till while condtions not matched")
while x <= 10: # while is checking x = 1 against 1 <= 10 and the ans is true, and running inside code.
    print(x) # print the 1st value 1 
    x = x + 1 # adding 1 + 1 + 2, x = 2 and now the loop continues. 


# what would happen if we do not add the increment line 
x = 1 
while x <= 10:
    print(x)
    # here we don't specify x = x + 1, it'll never add up to 10 <= 10 to end the while loop, so while loop will run infinetly 
       
       
    



"control flow statements:- if, for, while"

# nesting the if statements 
x = "cisco"
if "i" in x: # checking if i exists in the string 
    if len(x) > 3: #checking if string is greater than 
        print(x,len(x)) # if both if's are true then print 

# this above code can be written susing and operator 
x = "cisco"
if ("i" in x) and (len(x) > 3):
    print(x,len(x))
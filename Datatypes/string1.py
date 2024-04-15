a = "Cisco Switch"
strip_var = "   Cisco Switch  "
c = "$$Cisco Switch$$"
d = "  Root User "
split_string = "Cisco,Juniper,Palo alto,fortinet"
# string methods
""" index() :- finds the index no of the specified value in method
    find() :- finds the matching strings starting index no
    count() :- counts the no of elements in string
    upper() :- makes all uppercase
    lower() :- makes all lowercase
    startswith() :- finds vlaues starting with specified value in method
    endswith() :- finds values ending with specified value in method
    strip() :- removes empty spaces from string also specified values in that method
    replace() :- replaces the string values with specified values in method
    split() :- splits the values in string with specified delimeter in the method
    join() :- join the string with our specified value
    """
# find the index of the letter in string 

print(a.index("S")) # here we are printing index no of S from the variable a

# find how many times a letter is repeated
print(a.count("i")) # the output will be 2 because "i" repeated 2 times

# find starting index of matching string    
print("The starting index is:",a.find("Switch"))

# create string in upper and lower case 
print(a.lower())
print(a.upper())

# check start and end of the string is matching with our given values 
print("Value Cisco will match with string vlaue cisco and give value:",a.startswith("Cisco"))
print("Vlalue ch will match with ending value of string and give value:",a.endswith("ch"))
print("macbook does not match with string starting value cisco will give value:",a.startswith("macbook"))

# Removing empty scpaces from string 
print("Before: ", strip_var)
print("We are removing empty spaces from string:",strip_var.strip())

#Rmoving specific values from the string 
print("before: ",c)
print("We are removing $ signs :", c.strip("$"))

#Using replace to remove epmty space, but this will remove all empty space
print("before :",d)
print("We are removing all empty space :", d.replace(" ", "")) #Replacing "empty space" with ""
print("Replacing 'Root User' with 'common user' :",d.replace("Root", "Common")) # here we are replacing the "Root" value to "Common" value in string

#Using the split method to seperate string values by delimter
print("before :", split_string)
print("Splitting the values in string by delimiter ',' :", split_string.split(","))

#Using joi() to add value into the string
print("before :", a)
print("Using join to add underscor :", "_".join(a))
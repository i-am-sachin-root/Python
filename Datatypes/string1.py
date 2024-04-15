a = "Cisco Switch"
strip_var = "   Cisco Switch  "
c = "$$Cisco Switch$$"
d = "  Root User "
# string methods
""" index()
    find()
    count()
    upper()
    lower()
    startswith()
    endswith()
    strip()"""
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


a = "Cisco Switch"

# string methods
""" index()
    find()
    count()
    upper()
    lower()"""
# find the index of the letter in string 
print(a.index("S")) # here we are printing index no of S from the variable a

# find how many times a letter is repeated
print(a.count("i")) # the output will be 2 because "i" repeated 2 times

# find starting index of matching string    
print("The starting index is:",a.find("Switch"))

# create string in upper and lower case 
print(a.lower())
print(a.upper())

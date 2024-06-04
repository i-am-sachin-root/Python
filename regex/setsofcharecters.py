import re 
a = "123 Is a number, And 1234 is another number"
res = re.findall(r"[a-z]",a) #this will seperate the charecters and print in the list 
print(type(res))
print(res)

res = re.findall(r"[A-Z]",a) # this will find capital letters 
print(res)

res = re.findall(r"[ab]",a) # this will find a and b occurances  letters 
print(res)



res = re.findall(r"[^a]",a) # this will find all but ignore a  
print(res)


res = re.findall(r"[0-9]",a) # this will find all no in the string
print(res)
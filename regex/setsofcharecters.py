import re 
a = "123 is a number, and 1234 is another number"
res = re.findall(r"[a-z]",a) #this will seperate the charecters and print in the list 
print(type(res))
print(res)
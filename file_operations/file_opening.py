myfile = open("D:\\Python\\Mihai\\Python\\file_operations\\routers.txt", "r")
"""
r :- default mode :- read 
w :- write 
a :- append 
b :- binary 
x :- exclusive creation, used for photos, pdf, executable files etc (no text files basically)
"""

print(myfile.mode) #here we can see that in which mode we are opeining this file from r,w,a,b,x
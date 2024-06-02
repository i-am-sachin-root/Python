myfile = open("D:\\Python\\Mihai\\Python\\file_operations\\routers.txt", "r")
"""
r :- default mode :- read 
w :- write 
a :- append 
b :- binary 
x :- exclusive creation, used for photos, pdf, executable files etc (no text files basically)
"""

print(myfile.mode) #here we can see that in which mode we are opeining this file from r,w,a,b,x

#Reading the content of the file 
print(myfile.read()) 

#cursor position inside  the file
print(myfile.read(5)) # this will give no value because will be at the end of the file, so it won't give any values.


#change the postion of the cursor in the file
print(myfile.seek(0)) #this will reset the file at the start 

#check the current position of the cursor 
print(myfile.tell()) #this will tell that where is the currenlty cursor located in the file 


#now the cursor is at start so we can read from the start
print(myfile.read(5)) #here we are reading 5 charecters from the start of the file 

print(myfile.seek(0))

#reading first row of the file 
print(myfile.readline())

print(myfile.seek(0))

# Reading the entire file in list format 
print(myfile.readlines()) #this will print the file in list format 


#search specific workd in file 
myfile.seek(0) #going at the start
for line in myfile.readlines():
    
    if  line.startswith("Ci"):
        print(line)
        


    

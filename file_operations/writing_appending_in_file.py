"""
w :- will create file if does no exist, and will overwrite if does exist 
w+ :- for writing and reading with creation"""

file1 = open("D:\\Python\\Mihai\\Python\\file_operations\\test_write_append.txt", "w") #opening the file to write only 
file1.write("writing in the file \n ") #writing 
# file.writelines() can be used to get the data as a string 
file1.seek(0) #going at the start 
file1.close() #closing the file.
#print(file1.readlines()) #reading lines in the file 



### appending the data
file1 = open("D:\\Python\\Mihai\\Python\\file_operations\\test_write_append.txt", "a") # a for appending
file1.write("appending at the end \n ")
file1.close()


## check file is closed.
print(file1.closed) # returns true means file is closed


## assigning object to the file opening, when we use this we don't have to use close() method file auto closes 
with  open("D:\\Python\\Mihai\\Python\\file_operations\\test_write_append.txt", "a") as f :
    f.write("using assignement obsject to open the file")
print(f.closed) # checking that the file is auto closed or not 




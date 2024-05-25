"""try except else is used when code under try clause do not generate exceptions"""
try:
    print(4/2) #div is possible so no exceptions will be generated 
except NameError:
    print("Name Error") #print this if exceptions are generated  
else :
    print("No exceptions raised by try block ") # run else block if try block does not generate any exceptions



#finally clause :- works anyway same as except but try does not need to generate exception for runnig the finally clause 
try:
    print(4/2) #div is possible so no exceptions will be generated 
except NameError:
    print("Name Error") #print this if exceptions are generated  
finally : # this will generate the output anyways, try generates exception or not
    print("using finally to run the block anyway  ") # 
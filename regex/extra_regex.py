"""
\d :- digits \D :- any nondigit 
\s :- whitespaces
\w :- word
"""
import re

#non digit 
a = "google it"
t = re.search(r"\D+",a) #will find any nondigit characters 
t.group()
print(t)

#\S no whitespace 
t = re.search(r"\S+",a) #will stop after 1st white space becase it is inverse of finding white space
print(t)


#\W non word, will ignore words no and _
t = re.search(r"\W",a) #this will give 1st whitespace, can find all white spaces but need to use findall()
print(t)

# \A matches if the string starts with 
t = re.findall(r"\Ag",a) #this will check if the starting string matches with given expression
print(t) 

# \Z matching ending charecter 
t = re.findall(r"it\Z",a) #this will print it beacuse that is what matches with expression and in the string 
print(t)  

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
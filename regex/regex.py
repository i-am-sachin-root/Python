"""regular expression helps to find paatter inside a string 
Regular expression module:- re"""
import re 
mystr = "You can learn any programming language, whether it is Python2, Python3, Pearl, Java, javascript or PHP."

# match() method, finds matching at the begining of the scene
#sysntax
"""
var = re.match(pattern, string, optional flags"""
var1 = re.match("You",mystr)
print(var1)

#ignore cases in the string
var1 = re.match("you", re.I)
print(var1)
"""Exception handling helps to run rest of the code

under try block:- we add code that may cause exception at any given point while running the code 
 """

""""user try to get the exceptions, and user except to tell pyhton what to do if defined exceptions are occured"""
#using try to get ZeroDivision error
for i in range(5):
  try:
        print(i/0)
  except ZeroDivisionError as e: #here we are telling python what to so if ZeroDivision Error occured
      print(e,"Zerror Division error ouccured") #if Zero Division error occures then print/run the inside code block
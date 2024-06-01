from test_module import var1 #here we are using only what we need from the module, using * means import all  
import sys   
print(var1)

""""
Module search for import :- 1) build in modules are searched
                            2) searched in current dict
                            3) searched in path variables  """

#check available path variable where python finds its imp files
print(sys.path)
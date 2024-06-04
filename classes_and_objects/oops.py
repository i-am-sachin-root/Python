"object oriented programming based on calsses,objects and methods"
"class is a datatype containing it's attribute, vars and functions"
# we can use this to create many objects as possible and can assign code from the class so we don't need to write code again and again 
class MyRouter(object):
    "Info of the routers"
    ## constructor method for intialization of the attributes 
    def __init__(self,routername,model,serialno,ios): #construcotr creating to intialize the attrinute of and object 
        #definning paramaters 
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    #normal method borrows the attributes from the init method and uses in it's own code 
    def print_router(self,manuf_date):
        print("The router name is: ",self.routername)
        print("The router model is :",self.model)
        print("The serial no is :",self.serialno)
        print("The ios version is :",self.ios)
        print("The model no and date :",self.model + " ",manuf_date)

#creating 1st object 
router1 = MyRouter("R1","2600","123","16.2")
print(type(router1)) # here we have created an object 


#print the vale of the paramters 
print(router1.model)

#accessing the normal method 
print(router1.print_router("20240604"))
    
#get attribute value
at1 = getattr(router1,"routername")
print(at1)

#set attribute for new object 
router2 = MyRouter("Ver")
setattr(router2)





        
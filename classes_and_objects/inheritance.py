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

"Creating another class and inhereting from main class "

class MyNewRouter(MyRouter):
    "here we don't have to give init method becasue it is inhereting from parent "
    

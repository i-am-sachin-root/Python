dict2 = {"Vendor": "Cisco","Model":"2900","IOS":"12","gig ports":"2","FE ports":"4"}
print("Printing no of gig ports:",(dict2["gig ports"])) #this will print the value of the gig ports key 

#adding new key pair in dict
dict2["RAM"] = "256 MB"
print("Adding new key: pair in dict :",dict2)
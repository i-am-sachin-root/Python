dict2 = {"Vendor": "Cisco","Model":"2900","IOS":"12","gig ports":"2","FE ports":"4"}
print("Printing no of gig ports:",(dict2["gig ports"])) #this will print the value of the gig ports key 

#adding new key pair in dict
dict2["RAM"] = "256 MB"
print("Adding new key: pair in dict :",dict2)

#modefying the vlaue from the dict 
dict2["RAM"] = "512" # lets say we added extra dim of 256 
print("Modefied key vlaue :",dict2)

#deleting the key pair from the dict
del dict2["RAM"]
print("Deleted RAM key pair from the dict :",dict2)

#finding leght of the dict
print(dict2)
print("len of dict :",len(dict2))

#check if the value is in dict or not 
print(dict2)
print("checking if the key pair is available or not :",("gig ports" in dict2))
print("checking if the key pair is available or not :",("RAM" in dict2)) #this will give us value false because we have already deleted the RAM key par using del operator


#print the keys from the dict
print("Printing the keys from the dict :",dict2.keys())


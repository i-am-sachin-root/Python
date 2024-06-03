import re
arp = "Internet  192.168.1.1     4   0011.2233.4455  ARPA   Vlan1"

#matching ip add pattern in the string 

a = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", arp) # ip add expression 1-3digts.1-3digits.1-3dig.1-3dig, it will be in the form of the list. 
print(a)


# sub()
#used to replace in the string using regex,chages,stringname. we can change using regular expression 
b = re.sub(r"\d", "0", arp) # change all no in the arp var into 0
print(b)
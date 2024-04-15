# Cisco model: 2900/k9, 2 WAN slots, IOS 14.0
"""1) Place holders (old tyoe)
        %s :- holds the string 
        %d :- holds the integer 
        %f :- holds the float value 
    2) using {} for holding value
        .format(values):- add values to be hold in braces
    3) using {0} and index no to chose which value needs to be assigned where   """

print("Cisco model: %s,%d WAN slots,IOS %f" % ("2009/k9",2,14.0)) # here we are using placeholders and then values in paras will assigned to them.
#controling floating points for %f
print("Cisco model: %s,%d WAN slots,IOS %.2f" % ("2009/k9",2,14.0)) # Using %.2f will allow only 2 decimals after .
print("Cisco model: %s,%d WAN slots,IOS %.f" % ("2009/k9",2,14.0)) # Using %.f will allow 0 decimals after .

# We can use {} for hlding the value
print("Cisco model: {},{} WAN slots,IOS {}".format("2009/k9",2,14.0)) # {} will hold values from the braces

# We will use index no in braces to change sequence of values in string
print("Cisco model: {1},{0} WAN slots,IOS {2}".format("2009/k9",2,14.0)) #here output will 14, 2009/k9, 14.0

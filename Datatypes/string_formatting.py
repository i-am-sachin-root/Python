# Cisco model: 2900/k9, 2 WAN slots, IOS 14.0
"""Place holders (old tyoe)
        %s :- holds the string 
        %d :- holds the integer 
        %f :- holds the float value """

print("Cisco model: %s,%d WAN slots,IOS %f" % ("2009/k9",2,14.0)) # here we are using placeholders and then values in paras will assigned to them.
#controling floating points for %f
print("Cisco model: %s,%d WAN slots,IOS %.2f" % ("2009/k9",2,14.0)) # Using %.2f will allow only 2 decimals after .
print("Cisco model: %s,%d WAN slots,IOS %.f" % ("2009/k9",2,14.0)) # Using %.f will allow 0 decimals after .
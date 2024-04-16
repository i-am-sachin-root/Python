"""Positve index slicing 
    string = "somethin to be written"
    string[0 : 8] :- start and end of the index 
                    - [ :8] :- start from start and end at 8, vice versa

   Negative index slicing 

   Steps[::no] 
"""

string1 = "O E2   192.168.1.0 [110/20] via 10.0.0.1, 00:00:15, GigabitEthernet0/1"

print("Printing ip address from the routing table :", string1[7:18] ) #here we are using start index and end index to fetch the ip add 

# define starting index and end of the line 
print("Printing ip address from the routing table :", string1[7: ] ) #here we have not defined the end index so it will print till the end 

# define end index but not start index 
print("Printing ip address from the routing table :", string1[: 18] ) # here line will start from index 0 and will end on index 18(excluded)

# deine steps so that string will skip the letters 

print("using steps elements of string will be skipped :",string1[::4]) # output will be given with every 4 element skipped
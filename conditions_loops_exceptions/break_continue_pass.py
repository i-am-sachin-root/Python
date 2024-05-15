""" break and continue used in for and while loop to control the flow"""

# break :- used to terminate loop in which is resides

for no in range(10): #print no 0 to 9
    if no == 7: #checking the no is 7 or not 
        break #if no value is 7 then break the code 
    print(no) #print the last value of the no var
        

list1 = [4,5,6]
list2 = [10,20,30]

for i in list1: #taking element from list1 
    for j in list2: #taking element from list2
        if j == 20: #checking if the lj var has reached list2 20 element 
            break # if j = 20 then break the loop
        print(i * j)
    print("outside of the isnide for loop")

"""in above example only insde loop will breake if j = 20, and then main for loop will go to next element till inside for loop reaches again j = 20"""
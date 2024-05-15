"""continue:- if we see it in for and while loop
            -   it will skipp the next part of code and will go to the next iteration of the loop """

list1 = [4,5,6]
list2 = [10,20,30]

for i in list1:
    for j in list2:
        if j == 20: #checking if the value of the j is 20 
            continue # if j = 20, then skipp the next multiplication and got to main for loop for next iteration.
        print(i * j)
    print("outside of the inside for loop")

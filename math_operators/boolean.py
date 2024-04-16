"""
    Booleans :- TRUE and FALSE
    AND :- both sides need to be true 
    OR :- only one side needs to be true 
    NOT 
    """

num1 = 4
num2 = 3 

print("are num1 and num2 equal :",num1 == num2 ) # checking if they are equal or not
print("They are not eaqual :", num1 != num2) # check if they are not equal
print("Is num1 > than or equal to num2 :", num1 >= num2) # checking return true if num1 is > or == 

# AND operator 
print("AND operation work is values are equal :", 1==1 and 2==2) # left side and right side = true, if both true then ans = true 
print("AND operation work if vlaues not equal :", 1==3 and 2==2) # here final value false, because 1 and 3 not equal

# OR operator :- only one side needs to be true
print("OR operator :",num1 > num2 or num1 == num2 ) # only left side is true 



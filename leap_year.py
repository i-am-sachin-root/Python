""" def is_leap(year):
    #leap = False
    
    if (year % 4) != 0:
        print("False")
    elif (year % 100) != 0:
        print("leap")
    elif (year % 400) == 0:
        print("leap")
    else:
        print("False") 

year = int(input())
print(is_leap(year)) """

def is_leap(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) == 0:
        return True
    else:
        return False

year = int(input("Enter year: "))
print(is_leap(year))

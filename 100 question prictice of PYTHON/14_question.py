# Take user input of the year: example 2024
# print: 2024 is a/ is not a leap yrar

# criteria:
# 1. should be dicisible by 4, and not by 100
# 2. or, should be divisible by 400
# 
# featyre of use 
# funcation
# .....
# .....
# 
# 


def is_leap_year(year):
    if (year%4 == 0 and year%100 !=0) or (year%400== 0):
        return True
    else:
        return False
    

user_year = input("enter the yrae here: ")
if is_leap_year(int(user_year)):
    print(f"{user_year} is a leap year")
else:
    print(f"{user_year} is not a leap year")

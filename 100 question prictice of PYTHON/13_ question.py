# input 12345
# output = 1+2+3+4+5

#use
#list comprehence
# F-string

# asitional task 
# 1.Take input from user

# number = 23456
number = input("enter your number to add: ")
str_number = str(number)

sum_nums = sum(int(digit) for digit in str_number)
print (f"Sum of all digit of {number} is {sum_nums}")
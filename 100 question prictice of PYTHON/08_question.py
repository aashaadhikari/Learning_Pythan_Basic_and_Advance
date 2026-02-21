# calculate the factorial of a given number
# example: 4 factroial  = 4* 3*2*1, Factorial of 1 and 0 = 1

# use:
# 1. user input
# 2. function
# 3. f_string

def factorial (number):
    factorial = 1
    for i in range(2, number+1):
        factorial = factorial*i

    return factorial    


user_input = int(input("enter the number: "))
fac_numb = factorial(user_input)
print(f" factroial of {user_input} is {fac_numb} ")

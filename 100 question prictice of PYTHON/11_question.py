# Take two number inputs from, print the sum

def add_nums(num1, num2):
    sum = num1 + num2
    return sum 

first_input = int(input(" Enter first number: "))
second_input = int(input(" Enter second number:"))

sum = add_nums(first_input, second_input)
print(f"{first_input} and {second_input} sum is: {sum}")
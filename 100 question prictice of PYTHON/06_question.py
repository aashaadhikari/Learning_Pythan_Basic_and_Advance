# Check if a user input is prime
# prime number is only divisible by 1 and itself
# 1 is not a prime number

# 1. user input
# 2. function
# 3. f_string

# Additional tasks -> optimize the program

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number%i == 0:
            return False  
    return True    

number = int(input("Enter the number:"))

if is_prime(number):
    print(f"{number} is prime")

else:
    print(f"{number} is not prime")
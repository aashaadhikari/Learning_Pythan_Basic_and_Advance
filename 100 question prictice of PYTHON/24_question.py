# Python program to solve Quadratic Equation

# Quadratic Equation ax ** bX + C = 0
#  a, b , c is real number
#  a! = 0

# import cmath

# a = int(input("Enter posative number"))
# b = int(input("Enter number"))
# c = int(input("Enter number"))

# d = b**2 - 4*a*c

# root1 = (-b-cmath.sqrt(d))/(2*a)
# root2 = (-b+cmath.sqrt(d))/(2*a)

# print(f" the root are {root1} and {root2}")


# Using funcation


import cmath  # Import complex math module for complex roots


# Function to solve quadratic equation
def solve_quadratic(a, b, c):

      # Calculate the discriminant

    d = b**2 - 4*a*c 
    root1 = (-b-cmath.sqrt(d))/(2*a)
    root2 = (-b+cmath.sqrt(d))/(2*a)
    return root1, root2

print("Quadratic Equation: ax² + bx + c = 0")

# Taking input from user
a = float(input("Enter value of a (a ≠ 0): "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

if a == 0:
    print("Value of 'a' cannot be zero for a quadratic equation.")

else:
     # Call the function
    root1, root2 = solve_quadratic(a, b, c)


    # Display the results
    print(f"The roots of the quadratic equation are: {root1} and {root2}")
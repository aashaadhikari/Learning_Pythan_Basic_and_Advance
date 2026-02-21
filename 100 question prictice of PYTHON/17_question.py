# Calculate LCM(Least Common Multiple)
# Example: LCM of 6, 8 is 24
# Formula: a*b = GCD(a,b)* LCM(a,b)

# USE:
# Funcation
# f-string

# Additional Task
# 1. Calculate LCM of user Input 

import math

def cal_lcm(a,b):
    gcd = math.gcd(a,b)
    lcm = (a*b)//gcd
    return lcm

a = int(input("Enter the first number: "))
b= int(input("Enter the second number: "))

lcm = cal_lcm(a,b)
print(f"LCM of {a}, {b} is {lcm}")

# Calculate GDC(Greatest Common Divisor), use Euclidean Algorithm
# Example: GCD of 24 and 36 is 12

# use:
# 1. Funcation
# 2. Tuple Assignment

a = 12
b = 36

def cal_gcd(num1, num2):
    while(num2):
        print('starting')
        print(num1)
        print(num2)
        num1, num2 = num2, num1%num2
        print('After %')
        print(num1)
        print(num2)

    return num1

gcd = cal_gcd(a,b)
print(f"GCD of {a} and {b} is {gcd}")
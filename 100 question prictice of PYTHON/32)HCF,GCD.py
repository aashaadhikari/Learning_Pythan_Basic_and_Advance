# Find HCF or GCD

def find_hcf(x,y):
    if x >y:
        smaller =y

    else:
        smaller = x

    for i in range(1, smaller+1):
        if(x%i == 0 ) and (y%i == 0):
            hcf = i

    return hcf
user = int(input("Enter the first number: "))
user1 = int(input("Enter the second number: "))

print(f"the HCF of the given two number is {find_hcf(user, user1)}")
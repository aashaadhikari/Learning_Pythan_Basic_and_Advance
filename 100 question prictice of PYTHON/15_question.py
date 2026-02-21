# Armstrong number: 153
# how ? length of 153 = 3
# 1^3 + 5^3 +3^3 = 153

# Additional Task: 
# 1. create funcation
#2. Take user Input


def armstrong(number):
    len_num = len(number)
    arm_strongnum = sum(int(digit)** len_num for digit in number)
    if int(number) == arm_strongnum:
        return True

    else:
       return False   

number = (input("Enter the number: "))

if armstrong(number):
   print(f"{number} is an armstrong number ")

else:
    print(f"{number} is not armstrong number")   


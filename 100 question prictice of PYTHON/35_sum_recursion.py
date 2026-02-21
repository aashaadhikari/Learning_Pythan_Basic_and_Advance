

def naturalnumber(n):
    if n <= 1:
        return 1
    else:
        return ((n)+naturalnumber(n-1))
    

n = int(input("enter the number hear: "))
if n <= 0:
    print("Enter posative number: ")

else:
    print(f"The sum of natural number upto given number is {naturalnumber(n)} ")   
# A string is palindrome if the reverse of string is same as the orginal string 
# Example racecar == racecar(reverse)

# Use:
# 1. user input
# 2. funcrion
# 3. f- string

def is_palindrom(astring):
    astring = astring.lower()
    reversed_st = astring[::-1]
    if astring == reversed_st:
       return True
    else:
        return False


astring = str(input("Enter your string"))

if(is_palindrom(astring)):
    print(f"{astring} is a palindrome")
else:
    print(f"{astring} is not palindrome")
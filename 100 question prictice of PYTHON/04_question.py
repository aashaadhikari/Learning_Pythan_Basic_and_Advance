#    *
#   ***
#  *****
# *******
#*********



rows = 5
for i in range(1, rows+1):       # you need to use loop
    # print space
    print(" "* (rows - i), end="")

    # print *
    print("*"*(2*i-1))
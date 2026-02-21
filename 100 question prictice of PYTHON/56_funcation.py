# FUNCATION WITH *args

# write a funcation that takes variable number of arguments and return their sum.

def sum_all(*args):
    return sum(args)


print(sum_all(1, 2))
print(sum_all(1, 2, 4, 5, 6, 7))
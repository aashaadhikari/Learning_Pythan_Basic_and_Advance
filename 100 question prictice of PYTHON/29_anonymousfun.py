# Python program to display power of 2 using Anonymous Funcation
# also called lambda funcation

nterms = int(input("Enter the number of terms here: "))


result = list(map(lambda x : 2 ** x, range(nterms+1)))
# print(result) result come in list

for i in range(nterms+1):
    print("the value of 2 raised to power", i, "is", result[i])

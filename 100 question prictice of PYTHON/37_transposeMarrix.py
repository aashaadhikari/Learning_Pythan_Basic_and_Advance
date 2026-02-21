# solution 1 using for loop


a = [[1, 2, 3],
     [5, 7, 8]]

t = [[0, 0],
     [0, 0],
     [0, 0]]


for i in range(len(a)):
    for j in range(len(a[0])):
        t[j][i] = a[i][j]

for r in t:
    print(r)

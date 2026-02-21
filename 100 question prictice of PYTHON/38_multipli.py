a = [[1, 4, 6],
     [3, 5, 8],
     [7, 2, 6]]


b = [[5, 7, 8, 6],
    [8, 1, 2, 7],
    [9, 4, 6, 3]]


result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]


for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]


for i in result:
    print(i)



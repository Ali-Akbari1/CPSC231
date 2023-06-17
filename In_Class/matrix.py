a = [[2, 3], [4, 5]]
b = [[1, 3], [5, 7]]
c = [[0, 0], [0, 0]]

# determinant of 2 by 2 matrix

print(a[0][0]*a[1][1] - a[0][1]* a[1][0])

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = a[i][j] + b[i][j]

print(c)

# multiplication of two matrices

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j] = a +b ## complete this line

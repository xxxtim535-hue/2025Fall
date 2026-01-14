n, m1, m2 = map(int, input().split())
matrix1 = {}
matrix2 = {}
for _ in range(m1):
    i, j, value = map(int, input().split())
    matrix1[(i, j)] = value
for _ in range(m2):
    i, j, value = map(int, input().split())
    matrix2[(i, j)] = value
matrix3 = {}
tmp = 0
for i in range(n):
    for j in range(n):
        for y in range(n):
            a1 = matrix1.get((i, y), 0)
            a2 = matrix2.get((y, j), 0)
            tmp += a1*a2
        matrix3[(i, j)] = tmp
        tmp = 0

for i in range(n):
    for j in range(n):
        value = matrix3.get((i, j), 0)
        if value != 0:
            print(" ".join(map(str, [i, j, value])))
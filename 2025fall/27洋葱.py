n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = (n+1)//2
max_sum = 0
for i in range(m-1):
    left = i
    right = n-i
    sum = 0
    for j in range(left, right):
        sum += matrix[i][j]
        sum += matrix[n-i-1][j]
    for k in range(i+1, right-1):
        sum += matrix[k][left] + matrix[k][right-1]
    max_sum = max(max_sum, sum)
if n % 2 == 0:
    sum = matrix[m-1][m-1] + matrix[m-1][m] + matrix[m][m-1] + matrix[m][m]
    max_sum = max(max_sum, sum)
else:
    max_sum = max(max_sum, matrix[m-1][m-1])

print(max_sum)


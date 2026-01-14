m, n, p, q = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(m)]
kernel = [list(map(int, input().split())) for _ in range(p)]
out_rows = m - p + 1
out_cols = n - q + 1

result = []

for i in range(out_rows):
    row_result = []
    for j in range(out_cols):
        total = 0
        for ki in range(p):
            for kj in range(q):
                total += matrix[i + ki][j + kj] * kernel[ki][kj]
        row_result.append(total)
    result.append(row_result)

for row in result:
    print(' '.join(map(str, row)))

def read_matrix():
    row, col = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(row)]
    return matrix, row, col

def multiply(A, B, a_row, a_col, b_row, b_col):
    if a_col != b_row:
        return None
    result = [[0] * b_col for _ in range(a_row)]
    for i in range(a_row):
        for j in range(b_col):
            total = 0
            for k in range(a_col):
                total += A[i][k] * B[k][j]
            result[i][j] = total
    return result

def add(M1, M2):
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        return None
    result = []
    for i in range(len(M1)):
        row = []
        for j in range(len(M1[0])):
            row.append(M1[i][j] + M2[i][j])
        result.append(row)
    return result

A, a_row, a_col = read_matrix()
B, b_row, b_col = read_matrix()
C, c_row, c_col = read_matrix()

AB = multiply(A, B, a_row, a_col, b_row, b_col)
if AB is None:
    print("Error!")
else:
    result = add(AB, C)
    if result is None:
        print("Error!")
    else:
        for row in result:
            print(' '.join(map(str, row)))

path = []
result = []

def is_safe(a, b, path):
    for row, col in enumerate(path):
        if b == col or abs(row - a) == abs(col - b):
            return False
    return True
def backtrace(row):
    if row == 8:
        result.append(path.copy())
        return

    for col in range(8):
        if is_safe(row, col, path):
            path.append(col)
            backtrace(row+1)
            path.pop()
backtrace(0)
n = int(input())
for _ in range(n):
    m = int(input())
    tmp = result[m-1]
    temp = ''.join([str(x+1) for x in tmp])
    print(temp)
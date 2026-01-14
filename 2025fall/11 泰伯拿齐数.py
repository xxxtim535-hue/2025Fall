def taibonaqi(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return taibonaqi(n - 1) + taibonaqi(n-2) + taibonaqi(n-3)

n = int(input())
print(taibonaqi(n))
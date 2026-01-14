def isprime(k):
    if k == 2:
        return True
    elif k % 2 == 0:
        return False

    _ = 3
    while _*_ <= n:
        if n % _ == 0:
            return False
        _ += 2
    return True

n = int(input())
for i in range(2, n//2 + 1):
    if isprime(i) and isprime(n-i):
        print(f"{i} {n-i}")
        break
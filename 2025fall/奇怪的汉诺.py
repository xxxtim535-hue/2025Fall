def solve():
    f3 = [0]*13
    for i in range(13):
        f3[i] = 2**i - 1

    f4 = [0]*13
    f4[1] = 1

    for n in range(2, 13):
        f4[n] = float("inf")
        for k in range(1, n+1):
            moves = 2*f4[n-k] + f3[k]
            if moves < f4[n]:
                f4[n] = moves

    for n in range(1, 13):
        print(f4[n])

if __name__ == "__main__":
    solve()
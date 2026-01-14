from collections import deque
def solve():
    n, m = map(int, input().split())
    ind = [0] * n
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int ,input().split())
        g[a].append(b)
        ind[b] += 1

    q = deque()
    for i in range(n):
        if ind[i] == 0:
            q.append(i)
    leng = 0

    while q:
        u = q.popleft()
        leng += 1
        for v in g[u]:
            ind[v] -= 1
            if ind[v] == 0:
                q.append(v)

    if leng == n:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    solve()
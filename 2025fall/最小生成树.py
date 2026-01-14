import sys
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    g = [set() for _ in range(n+1)]

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        g[a].add(b)
        g[b].add(a)

    rest = set(range(1, n+1))
    components = 0

    while rest:
        start = rest.pop()
        q = deque([start])
        components += 1
        while q:
            u = q.popleft()
            to_remove = []
            for v in rest:
                if v not in g[u]:
                    to_remove.append(v)
            for v in to_remove:
                rest.remove(v)
                q.append(v)

    print(components - 1)

if __name__ =="__main__":
    main()

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    ind = 0
    n = data[ind]; ind+=1
    m = data[ind]; ind+=1

    g = [set() for _ in range(n+1)]

    for _ in range(m):
        a = data[ind]; ind+=1
        b = data[ind]; ind+=1
        g[a].add(b)
        g[b].add(a)

    rest = set([i for i in range(1, n+1)])
    ###rest = set(range(1, n+1))
    ans = 0

    while rest:
        start = rest.pop()
        q = deque([start])
        ans += 1
        while q:
            u = q.popleft()
            rem = []
            for v in rest:
                if v not in g[u]:
                    rem.append(v)

            for v in rem:
                q.append(v)
                rest.remove(v)

    print(ans - 1)


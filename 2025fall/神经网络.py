from collections import deque,defaultdict
import sys

sys.setrecursionlimit(10000)
def main():
    n, p = map(int, input().split())
    initC = [0] * (n+1) #1
    U = [0] * (n+1)

    for _ in range(1, n+1):
        c, u = map(int, input().split())
        initC[_] = c
        U[_] = u

    graph = defaultdict(list)
    indegree = [0]*(n+1)
    outdegree = [0]*(n+1)
    weight_sum = defaultdict(int)

    for _ in range(p):
        i, j, w = map(int, input().split())
        weight_sum[(i, j)] += w

    for (i, j), w in weight_sum.items():
        graph[i].append(j)
        indegree[j] += 1
        outdegree[i] += 1

    indegree_copy = indegree[:]
    q = deque()
    for i in range(1, n+1):
        if indegree_copy[i] == 0:
            q.append(i)

    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in graph[u]:
            indegree_copy[v] -= 1
            if indegree_copy[v] == 0:
                q.append(v)

    if len(topo_order) != n:
        print("NULL")
        return

    C = [0] * (n+1)
    for i in range(1, n+1):
        if indegree[i] == 0:
            C[i] = initC[i]

    for u in topo_order:
        if indegree[u] > 0:
            C[u] = C[u] - U[u]
            if C[u] <= 0:
                continue

        if C[u] > 0:
            for v in graph[u]:
                w = weight_sum[(u, v)]
                C[v] += w * C[u]

    output = []
    for i in range(1, n+1):
        if outdegree[i] == 0 and C[i] > 0:
            output.append((i, C[i]))

    if not output:
        print("NULL")
    else:
        for i, val in sorted(output):
            print(i, val)

if __name__ == "__main__":
    main()
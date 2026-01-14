n, m, L = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
start = int(input())
visited = []

graph = dict((i, []) for i in range(n))
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

for dot in graph:
    graph[dot].sort()

def dfs(dot, depth):
    if depth > L:
        return
    visited.append(dot)
    for neighbor in graph[dot]:
        if neighbor not in visited:
            dfs(neighbor, depth + 1)

dfs(start, 0)
print(" ".join(map(str, visited)))

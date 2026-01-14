from collections import deque

def solve():
    import sys
    sys.setrecursionlimit(10000)### 这道题这个非常阴，m<=10000

    n,m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        graph[u].append((v, t))
        graph[v].append((u,t))

    color = [-1]*n

    for i in range(n):
        if color[i] == -1:
            q = deque([i])
            color[i] = 0
            while q:
                u = q.popleft()
                for v, t in graph[u]:
                    expected_color = color[u] if t == 0 else 1-color[u]
                    if color[v] == -1:
                        color[v] = expected_color
                        q.append(v)
                    elif color[v] != expected_color:
                        print("NO")
                        return    ###这里应当注意到，被赋予过颜色的点都是在q里面的，所以遇到有颜色的点直接检查颜色即可，不需要调整栈

    print("YES")

if __name__ == "__main__":
    solve()

###并查集：
import sys
sys.setrecursionlimit(10000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return root_x != root_y

def solve_two_set():
    """
    两倍空间法：
    对每个植物i创建两个元素：i (表示种类A) 和 i+n (表示种类B)
    如果结论说i和j相同：union(i, j) 和 union(i+n, j+n)
    如果结论说i和j不同：union(i, j+n) 和 union(i+n, j)
    检查矛盾：如果find(i) == find(i+n)，则矛盾
    """
    ###这样理解即可，前n个代表A，后n个代表B，相当于同时举了两种情况，当一种情况出现矛盾，最后就会出现一个物件同时出现在A和B
    data = sys.stdin.read().strip().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    dsu = DSU(2*n)

    for _ in range(m):
        x = int(data[idx]); idx+=1
        y = int(data[idx]); idx+=1
        relation = int(data[idx]); idx+=1

        if relation == 0:
            dsu.union(x, y)
            dsu.union(x+n, y+n)
        else:
            dsu.union(x, y+n)
            dsu.union(x+n, y)

    for i in range(n):
        if dsu.find(i) == dsu.find(i+n):
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    solve_two_set()









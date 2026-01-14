def find(x, parent):
    if parent[x-1] != x:
        parent[x-1] = find(parent[x-1], parent)
    return parent[x-1]
#find函数同时完成了寻找根函数同时做好路径压缩
def union(x, y, parent, rank):
    rootX = find(x, parent)
    rootY = find(y, parent)
    if rootX == rootY:
        return False
    if rank[rootX-1] < rank[rootY-1]:
        parent[rootX-1] = rootY
    elif rank[rootX-1] > rank[rootY-1]:
        parent[rootY-1] = rootX
    else:
        parent[rootY-1] = rootX
        rank[rootX-1] += 1
    return True

eg = 0
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    eg += 1
    count = a
    parent = list(range(1, a+1))
    rank = [0] * a
    for _ in range(b):
        c, d = map(int, input().split())
        if union(c, d, parent, rank):
            count -= 1
    print(f"Case {eg}: {count}")





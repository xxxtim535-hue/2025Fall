from collections import defaultdict, deque

n = int(input())
tree = defaultdict(list)
for _ in range(n):
    data = map(int, input().strip().split())
    tree[data[0]].extend(data[1:])

def name(root):
    data = [root] + tree[root]
    data.sort()
    q = deque(data)
import sys
from collections import deque

def build(pre, mid):
    if not pre: return ""
    root = pre[0]
    idx = mid.index(root)
    left = build(pre[1: idx+1], mid[:idx])
    right = build(pre[idx+1:], mid[idx+1:])

    return left + right + root

data = sys.stdin.read().strip().split("\n")
data = deque(data)

while data:
    pre, mid = data.popleft().split()

    print(build(pre, mid))


class Node:
    def __init__(self):
        self.child = {}
        self.end = False

def insert(root, s):
    cur = root
    for c in s:
        #已有的号码是当前号码前缀
        if cur.end:
            return False
        if c not in cur.child:
            cur.child[c] = Node()
        cur = cur.child[c]
    if cur.end:
        return False
    if cur.child:
        return False
    cur.end = True
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()

    root = Node()
    ok = True
    for num in nums:
        if not insert(root, num):
            ok = False
            break

    print("YES" if ok else "NO")
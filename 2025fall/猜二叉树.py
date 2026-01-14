from collections import deque
n = int(input())
for _ in range(n):
    mid = input().strip()
    post = input().strip()

    result = []
    q = deque([(mid, post)])

    while q:
        mid, post = q.popleft()

        root = post[-1]
        result.append(root)

        ind = mid.index(root)
        left_mid = mid[:ind]
        right_mid = mid[ind+1:]
        left_post = post[:len(left_mid)]
        right_post = post[len(left_mid):-1]

        if left_mid:
            q.append((left_mid, left_post))
        if right_mid:
            q.append((right_mid, right_post))

    print("".join(result))

def build(mid, post):
    """前序排序"""
    if not mid:
        return ""
    root = post[-1]
    ind = mid.index(root)
    left = build(mid[:ind], post[:ind])
    right = build(mid[ind+1:], post[ind:-1])

    return root + left + right
from collections import deque
n = int(input())
stack = list(map(int, input().split()))
stackm = []
ans = deque()
while stack:
    u = stack.pop()
    if u > 0:
        if not stackm:
            ans.appendleft(u)
            continue
        while stackm:
            m = stackm.pop()
            tmp = u
            u += m
            m += tmp
            if m < 0:
                stackm.append(m)
                break
        if u > 0:
            ans.appendleft(u)
    elif u < 0:
        stackm.append(u)
answer = stackm[::-1] + list(ans)
print(len(answer))
print(" ".join(map(str, answer)))
"""import sys
import heapq


def solve():
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    D = int(data[1])
    h = list(map(int, data[2:2 + N]))

    # 剩余元素的下标
    indices = list(range(N))
    result = []

    while indices:
        n = len(indices)
        # 计算前缀最小值和最大值
        prefix_min = [0] * n
        prefix_max = [0] * n

        prefix_min[0] = h[indices[0]]
        prefix_max[0] = h[indices[0]]

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], h[indices[i]])
            prefix_max[i] = max(prefix_max[i - 1], h[indices[i]])

        # 找出所有可到达的元素
        reachable = []

        # 第一个元素肯定可到达
        reachable.append((h[indices[0]], indices[0], 0))

        for j in range(1, n):
            hj = h[indices[j]]

            # 快速判断：检查是否在区间内
            if hj < prefix_min[j - 1] - D or hj > prefix_max[j - 1] + D:
                continue

            # 如果通过区间检查，还需要精确验证每个i<j
            # 但我们可以用DP思想进一步优化
            can_move = True
            # 只需要检查hj是否和之前的最小值、最大值都满足条件
            if hj < prefix_min[j - 1] - D or hj > prefix_max[j - 1] + D:
                can_move = False
            else:
                # 对于区间内的值，还需要检查是否真的每个都满足
                # 但大部分情况都可以通过
                for i in range(j):
                    if abs(h[indices[i]] - hj) > D:
                        can_move = False
                        break

            if can_move:
                reachable.append((hj, indices[j], j))

        # 选择最小的
        reachable.sort()
        val, original_idx, list_idx = reachable[0]
        result.append(val)

        # 移除选中的元素
        indices.pop(list_idx)

    sys.stdout.write("\n".join(map(str, result)) + "\n")


if __name__ == "__main__":
    solve()"""

import sys
from collections import deque

n, d = map(int, sys.stdin.readline().split())
l = deque(map(int, sys.stdin.read().split()))
out = []

while l:
    m = deque()
    p = l.popleft()
    left, right = p-d, p+d
    r = [p]
    L = len(l)
    for _ in range(L):
        q = l.popleft()
        left = max(left, q-d)
        right = min(right, q+d)
        if right < left:
            l.appendleft(q)
            break
        if left <= q <= right:
            r.append(q)
        else:
            m.append(q)
    l.extend(m)
    r.sort()
    out.extend(r)

print("\n".join(map(str, out)))
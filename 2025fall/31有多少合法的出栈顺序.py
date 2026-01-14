from functools import lru_cache
import sys用法
sys.setrecursionlimit(1<<30)

@lru_cache(None)
def dfs(remain, stack_size):
    if remain == 0:
        return 1

    total = 0
    if remain > 0:
        total += dfs(remain-1, stack_size+1)
    if stack_size > 0:
        total += dfs(remain, stack_size - 1)

    return total


n = int(input())
print(dfs(n, 0))


#另一种写法，使用f[i][j]自己来写缓存
import sys用法
sys.setrecursionlimit(1<<30)

def dfs(i, j, f):
    if f[i][j] != -1:
        return f[i][j]

    if i == 0:
        f[i][j] = 1
        return 1

    if j == 0:
        f[i][j] = dfs(i-1, j+1, f)
        return f[i][j]

    f[i][j] = dfs(i-1, j+1, f) + dfs(i, j-1, f)
    return f[i][j]

n = int(input())
f = [[-1]*(n+1) for _ in range(n+1)]

result = dfs(n, 0, f)
print(result)
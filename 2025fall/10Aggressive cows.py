def can(mid):
    count = 1
    cur = xs[0]
    for i in range(1, N):
        if xs[i] - cur >= mid:
            count += 1
            cur = xs[i]
    return count >= C
#存在右界必须验证是否可行的问题
def half_sort(xs):
    left = 1
    right = (xs[-1] - xs[0])//(C - 1)
    while left <= right:
        mid = left + (right-left)//2
        if can(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

N, C = map(int, input().split())
xs = sorted([int(input()) for _ in range(N)])
print(half_sort(xs))
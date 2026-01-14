def can(a, lis, maxop):
    plus = 0
    val = 0
    for _ in range(N):
        plus += lis[_]
        if plus > a:
            plus = lis[_]
            val += 1
    if plus <= a:
        val += 1
    if val > maxop:
        return False
    else:
        return True

N, M = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]
l = max(nums)
r = sum(nums)

while r > l:
    mid = l + (r - l)//2
    if can(mid, nums, M):
        r = mid - 1
    else:
        l = mid + 1

print(l)

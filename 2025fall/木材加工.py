n, k = map(int, input().split())
total = 0
wood = []
for _ in range(n):
    length = int(input().strip())
    total += length
    wood.append(length)

max_ = total//k
left, right = 1, max_
while left <= right:
    mid = (left + right) // 2
    if sum(log//mid for log in wood) >= k:
        left = mid+1
    else:
        right = mid-1

print(right)

"""二分法需要注意的是边界。符合条件的时候left = mid+1，所以left最后一定大于标准值，而right是不行的时候再减一
这就意味着不可能出现一定不行，最后一定是要输出right"""
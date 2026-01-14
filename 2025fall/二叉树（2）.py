a, b = map(int, input().strip().split())
while a and b:
    left, right = a, a
    count = 0
    while left <= b:
        count += min(right, b) - left + 1
        left = left*2
        right = right*2 + 1
    print(str(count))
    a, b = map(int, input().strip().split())

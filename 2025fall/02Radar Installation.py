import math
def merge_sort(points):
    if len(points) <= 1:
        return points

    mid = len(points)//2
    left = merge_sort(points[:mid])
    right = merge_sort(points[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

case = 1
while True:
    line = input()
    if line == '':
        continue
    else:
        a, d = map(int, line.split())
        if a == 0 and d == 0:
            break

    points = [list(map(int, input().split())) for _ in range(a)]

    cases = merge_sort(points)

    num = 0
    k = 0
    xr = cases[k][0] - d - 1
    flag = 0
    while a>k:
        x = cases[k][0]
        y = cases[k][1]
        if y > d:
            print("Case ", case, ":", -1)
            flag = 1
            break
        elif (xr - x)**2 + y**2 > d**2 and x > xr:
            xr = x + math.sqrt(d**2 - y**2)
            num += 1

        k += 1
    if flag == 0:
        print(f"Case {case}: {num}")
    case += 1
#爆完了，从第一个岛开始贪心雷达位置是做不到的（悲）

#标答，每个岛对应的最大雷达范围，排序
import math

def solve(n, d, islands):
    if d < 0:
        return -1

    ranges = []
    for x, y in islands:     #元组可以直接等
        if y > d:
            return -1
        delta = math.sqrt(d * d - y * y)
        ranges.append((x - delta, x + delta))

    if not ranges:
        return -1

    ranges.sort(key=lambda x:x[1])

    number = 1
    r = ranges[0][1]
    for start, end in ranges[1:]:
        if r < start:
            r = end
            number += 1

    return number

case_number = 0
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break

    case_number += 1
    islands = []
    for _ in range(n):
        islands.append(tuple(map(int, input().split())))

    result = solve(n, d, islands)
    print(f"Case {case_number}: {result}")
    input()

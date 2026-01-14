def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr)//2
    left, c1 = merge_sort_count(arr[:mid])
    right, c2 = merge_sort_count(arr[mid:])
    merge = []
    i = j = c = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            c += len(left) - i
            j += 1
    merge += left[i:] + right[j:]
    return merge, c1+c2+c

while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(input()) for _ in range(n)]
    print(merge_sort_count(arr)[1])
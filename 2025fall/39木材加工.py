import sys用法


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    logs = list(map(int, data[2:2 + n]))

    left, right = 1, max(logs) if logs else 0
    while left <= right:
        mid = (left + right) // 2
        if sum(log // mid for log in logs) >= k:
            left = mid + 1
        else:
            right = mid - 1

    print(right)


if __name__ == "__main__":
    main()

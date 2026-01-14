import sys用法

def main():
    data = sys.stdin.read().split()
    i = 0
    results = []
    while i < len(data):
        m = int(data[i])
        n = int(data[i + 1])
        i += 2
        if m == 0 and n == 0:
            break
        left = m
        right = m
        count = 0
        while left <= n:
            count += min(right, n) - left + 1
            left = left * 2
            right = right * 2 + 1
        results.append(str(count))
    print("\n".join(results))

if __name__ == "__main__":
    main()
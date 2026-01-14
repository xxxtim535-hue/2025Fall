import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    A = list(map(int, data[1:]))

    left = []
    right = []
    res = []

    for i in range(n):
        heapq.heappush(left, -A[i])

        if right and -left[0] > right[0]:
            max = -heapq.heappop(left)
            min = heapq.heappop(right)
            heapq.heappush(left, -min)
            heapq.heappush(right, max)

        if len(left) > len(right)+1:
            heapq.heappush(right, -heapq.heappop(left))

        if i % 2 == 0:
            res.append(str(-left[0]))

    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
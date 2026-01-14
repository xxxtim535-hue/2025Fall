import heapq

def huffman_tree(weights):
    heapq.heapify(weights)
    total = 0

    while len(weights) > 1:
        min1 = heapq.heappop(weights)
        min2 = heapq.heappop(weights)

        total += min1 + min2
        new = min1 + min2

        heapq.heappush(weights, new)

    return total
def main():
    n = int(input().strip())
    weights = list(map(int, input().strip().split()))

    result = huffman_tree(weights)
    print(result)

if __name__ == "__main__":
    main()
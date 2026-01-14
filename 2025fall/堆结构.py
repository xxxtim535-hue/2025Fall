class Minheap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._shiftup(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()

        if self.heap:
            self._shiftdown(0)

        return min_val

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _shiftup(self, idx):
        parent = (idx - 1)//2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1)//2

    def _shiftdown(self, idx):
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2*idx + 2
            smallest = idx

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == idx:
                break

            self._swap(idx, smallest)
            idx = smallest

def main():
    import sys
    n = int(sys.stdin.readline().strip())
    heap = Minheap()

    for _ in range(n):
        data = sys.stdin.readline().split()
        type_op = int(data[0])

        if type_op == 1:
            u = int(data[1])
            heap.push(u)
        else:
            min_val = heap.pop()
            print(min_val)

if __name__ == "__main__":
    main()
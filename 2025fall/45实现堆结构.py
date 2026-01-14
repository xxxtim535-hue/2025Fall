import sys用法

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        """插入元素"""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """删除并返回最小元素"""
        if not self.heap:
            return None

        # 将最小元素（堆顶）与最后一个元素交换
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()

        # 调整堆
        if self.heap:
            self._sift_down(0)

        return min_val

    def _sift_up(self, idx):
        """从下往上调整堆"""
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        """从上往下调整堆"""
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == idx:
                break

            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, i, j):
        """交换两个元素"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def main():
    n = int(sys.stdin.readline().strip())
    heap = MinHeap()

    for _ in range(n):
        data = sys.stdin.readline().split()
        type_op = int(data[0])

        if type_op == 1:
            # 插入操作
            u = int(data[1])
            heap.push(u)
        else:
            # 删除并输出最小元素
            min_val = heap.pop()
            print(min_val)


if __name__ == "__main__":
    main()
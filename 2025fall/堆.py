class Minheap:
    def __init__(self):
        self.heap = []

    def push(self, new):
        self.heap.append(new)
        self.shift_up(len(self.heap) - 1)

    def shift_up(self, num):
        parent = (num - 1)//2
        while num > 0 and self.heap[parent] > self.heap[num]:
            """使用num > 0作为判据"""
            self.heap[parent], self.heap[num] = self.heap[num] ,self.heap[parent]
            num = parent
            parent = (parent - 1)//2

    def pop(self):
        if not self.heap:
            return None

        n = len(self.heap) - 1
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0]

        min_val = self.heap.pop()

        self.shift_down(0)
        return min_val

    def shift_down(self, num):
        n = len(self.heap) - 1
        while 2*num + 1 <= n:
            left = 2*num +1
            right = 2*num + 2
            small = num
            if self.heap[left] < self.heap[small]:
                small = left
            if right <= n and self.heap[right] < self.heap[small]:
                small = right
            if num == small:
                break
            else:
                self.heap[num], self.heap[small] = self.heap[small], self.heap[num]
                num = small

def main():
    n = int(input())
    heap1 = Minheap()
    for _ in range(n):
        data = input().split()
        if int(data[0]) == 1:
            heap1.push(int(data[1]))
        else:
            inte =  heap1.pop()
            print(inte)

if __name__ == "__main__":
    main()


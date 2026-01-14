from sys用法 import stdin
from collections import deque, defaultdict

def main():
    n = int(stdin.readline())
    forest_post_order = []

    for _ in range(n):
        data = stdin.readline().split()
        if not data:
            continue

        nodes = []
        i = 0
        while i < len(data):
            ch = data[i]
            num = int(data[i+1])
            nodes.append((ch, num))
            i += 2

        queue = deque()
        queue.append(0)
        index = 1
        children = defaultdict(list)

        while queue:
            idx = queue.popleft()
            ch, num = nodes[idx]
            for _ in range(num):
                children[ch].append(nodes[index][0])
                if num != 0:
                    queue.append(index)
                index += 1

        def postorder(root):
            result = []
            for child in children[root]:
                result.extend(postorder(child))
            result.append(root)
            return result

        root = nodes[0][0]
        forest_post_order.extend(postorder(root))

    print(' '.join(forest_post_order))

if __name__ == "__main__":
    main()
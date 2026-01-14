from sys import stdin
from collections import deque, defaultdict

def main():
    n = int(stdin.readline())
    post = []

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

        q = deque()
        q.append(0)
        ind = 1
        children = defaultdict(list)

        while q:
            idx = q.popleft()
            ch, num = nodes[idx]
            for _ in range(num):
                children[ch].append(nodes[ind][0])
                if num != 0:
                    q.append(ind)
                ind += 1

        def postorder(root):
            result = []
            for child in children[root]:
                result.extend(postorder(child))
            result.append(root)
            return result

        root = nodes[0][0]
        post.extend(postorder(root))

    print(" ".join(post))

if __name__ == "__main__":
    main()
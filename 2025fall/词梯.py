from collections import defaultdict, deque
def main():
    n = int(input())
    g = defaultdict(list)
    pattern = defaultdict(list)

    for _ in range(n):
        word = input().strip()
        for i in range(4):
            patter = word[:i] + "*" + word[i+1:]

            for neibor in pattern[patter]:
                g[word].append(neibor)
                g[neibor].append(word)

            pattern[patter].append(word)

    a, b = input().strip().split()
    visited = defaultdict(bool)
    path = []

    """def dfs(node):
        if node == b:
            path.append(b)
            return path.copy()
    
        path.append(node)
        visited[node] = True
    
        for neibor in g[node]:
            if not visited[neibor]:
                result = dfs(neibor)
                if result:
                    return result
    
        path.pop()
        visited[node] = False
        dfs不行（
    """
    prev = {a: None}
    q = deque([a])

    while q:
        u = q.popleft()

        if u == b:
            break

        for neibor in g[u]:
            if neibor not in prev:###只记下来最快到达这个点的上一个点
                prev[neibor] = u
                q.append(neibor)
    if b not in prev:
        print("NO")
        return
    node = b
    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()
    print(" ".join(path))

if __name__ == "__main__":
    main()

from collections import deque

R, C, K = map(int, input().split())
matrix = [input().strip() for _ in range(R)]

start = end = None
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'S':
            start = (i, j)
        elif matrix[i][j] == 'E':
            end = (i, j)

neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [[[False] * (K + 1) for _ in range(C)] for _ in range(R)]

queue = deque()
sx, sy = start
queue.append((sx, sy, K, 0))
found = False
while queue:
    x, y, k_left, steps = queue.popleft()

    if (x, y) == end:
        print(steps)
        found = True
        break

    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0<=nx<R and 0<=ny<C:
            cell = matrix[nx][ny]
            nk_left = k_left
            if cell == '#':
                if k_left <= 0:
                    continue
                nk_left = k_left - 1

            if not visited[nx][ny][nk_left]:
                visited[nx][ny][nk_left] = True
                queue.append((nx, ny, nk_left, steps + 1))

if not found:
    print(-1)



from collections import deque
def bfs(matrix, R, C, start):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start[0], start[1], 0)])
    visited = [[False] *C for _ in range(R)]
    visited[start[0]][start[1]] = True
    result = -1

    while queue:
        x, y, time = queue.popleft()
        if matrix[x][y] == 'E':
            result = time
            break

        for dx, dy in directions:
            nx, ny = x + dx, y+dy
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and matrix[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny, time+1))

    return result

def main():
    n = int(input())
    for _ in range(n):
        row, col = map(int, input().split())
        matrix = []
        start = None
        for _ in range(row):
            R = input().strip()
            matrix.append(R)
            if not start:
                if "S" in R:
                    start = (_, R.index("S"))

        result = bfs(matrix, row, col, start)
        if result == -1:
            print("oop!")
        else:
            print(result)

if __name__ == "__main__":
    main()
def bfs(matrix, flag, R, C):
    from collections import deque
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(flag[0], flag[1], 0)])
    visited = [[False]*C for _ in range(R)]
    visited[flag[0]][flag[1]] = True

    while q:
        u, v, time = q.popleft()
        if matrix[u][v] == "E":
            return time

        for dx, dy in moves:
            nx, ny = u + dx, v + dy
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and matrix[nx][ny] != "#":
                visited[nx][ny] = True
                q.append((nx, ny, time+1))

    return False
def main():
    import sys
    data = sys.stdin.read().strip().split("\n")
    ind = 0

    T = int(data[ind]);ind+=1
    for _ in range(T):
        R, C = map(int, data[ind].split());ind += 1
        matrix = []
        flag = False

        for _ in range(R):
            row = data[ind].strip();ind += 1
            matrix.append(row)
            if not flag:
                if "S" in row:
                    flag = (_, row.index("S"))

        result = bfs(matrix, flag, R, C)
        if result:
            print(result)
        else:
            print("oop!")

if __name__ == "__main__":
    main()

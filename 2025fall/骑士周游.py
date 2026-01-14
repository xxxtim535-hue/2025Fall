def main():
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    n = int(input().strip())
    visited = [[False] * n for _ in range(n)]

    def valid(x, y):
        return 0 <= x < n and 0 <= y < n and not visited[x][y]

    def cnt(x, y):
        count = 0
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if valid(nx, ny):
                count += 1

        return count

    def dfs(x, y, steps):
        if steps == n*n:
            return True

        next_moves = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if valid(nx, ny):
                count = cnt(nx, ny)
                next_moves.append((count, nx, ny))

        next_moves.sort(key=lambda t: t[0])

        for _, nx, ny in next_moves:
            visited[nx][ny] = True
            if dfs(nx, ny, steps+1):
                return True
            visited[nx][ny] = False

        return False

    sr, sc = map(int, input().split())
    visited[sr][sc] = True

    if dfs(sr, sc, 1):
        return "success"
    else:
        return "fail"

if __name__ == "__main__":
    print(main())

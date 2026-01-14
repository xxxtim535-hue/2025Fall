#为每一个坐标标定一个相对位置高度dp，这样从最低的开始标为1，一步一步下去


R, C = map(int, input().split())
dp = [[1 for _ in range(C)] for _ in range(R)]
grid = []
for _ in range(R):
    grid.append(list(map(int, input().split())))
# 这里可以用grid = [list(map(int, input().split())) for _ in range(R)]
#从小到大排序
points = sorted([(grid[i][j], i, j) for i in range(R) for j in range(C)])

directions = [(0,1), (0,-1), (1,0), (-1,0)]

long = 1

for height, x, y in points:
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if 0<=xn<R and 0<=yn<C and grid[xn][yn] < height:
            dp[x][y] = dp[x][y] if dp[x][y] > dp[xn][yn] + 1 else dp[xn][yn] + 1
    long = max(dp[x][y], long)

print(long)








k = int(input())
for case in range(k):
    m, n = map(int, input().split())
    ans = 'A1'
    matrix = [[0]*n for _ in range(m)]
    matrix[0][0] = 1
    neighbors = [(-1, -2),(1,-2),(-2,-1),(2,-1),(-2,1),(2,1),(-1,2),(1,2)]
    found = False
    def dfs(i, j):
        global found,ans
        if len(ans) == 2*m*n:
            found = True
            return

        for dx, dy in neighbors:
            if 0 <= i+dx < m and 0<=j + dy<n:
                if matrix[i+dx][j+dy] == 0:
                    ans += chr(ord('A')+j+dy) + str(i+dx+1)
                    matrix[i+dx][j+dy] = 1
                    dfs(i+dx, j+dy)
                    if found:
                        return
                    ans = ans[:-2]
                    matrix[i+dx][j+dy] = 0
    dfs(0,0)
    print(f"Scenario #{case+1}:")
    if len(ans) == 2*m*n:
        print(ans)
    else:
        print("impossible")
    if case != k-1:
        print()
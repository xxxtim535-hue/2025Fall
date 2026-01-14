n = int(input())

dp = [0] * 51
dp[0] = 1

for j in range(1, 51):
    """划分中最大的数字j"""
    for i in range(j, 51):
        dp[i] += dp[i-j]

print(dp[n])
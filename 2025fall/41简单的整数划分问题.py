import sys用法

def main():
    max_n = 50
    dp = [0] * (max_n + 1)
    dp[0] = 1  # 基础情况：0的划分数为1（空划分）

    # 动态规划计算划分数：类似完全背包问题
    for j in range(1, max_n + 1):
        for i in range(j, max_n + 1):
            dp[i] += dp[i - j]

    # 读取多组输入并输出结果
    data = sys.stdin.read().split()
    for n_str in data:
        n = int(n_str)
        print(dp[n])

if __name__ == '__main__':
    main()
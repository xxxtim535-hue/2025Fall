import sys

input = sys.stdin.read
output = sys.stdout.write
"""这里是在重新定义函数input 和 output"""
def solve():
    data = input().split()
    n = int(data[0])
    results = []
    for i in range(1, n + 1):
        # 假设是简单的加法运算
        results.append(str(int(data[2*i - 1]) + int(data[2*i])))
    output("\n".join(results) + "\n")

solve()
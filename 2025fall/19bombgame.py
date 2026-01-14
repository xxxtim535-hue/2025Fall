#chaos
from collections import defaultdict

A, B, K = map(int, input().split())
dictionary = defaultdict(int)
for _ in range(K):
    R, S, P, T = map(int, input().split())
    if T == 1:
        for i in range(R - (P - 1)//2 - 1, R + (P - 1)//2):
            for j in range(S - (P - 1)//2 - 1, S + (P - 1)//2):
                if A> i >= 0 and B > j >= 0 and (i, j):
                    dictionary[(i, j)] += 1
    else:
        for i in range(R - (P - 1)//2 - 1, R + (P - 1)//2):
            for j in range(S - (P - 1)//2 - 1, S + (P - 1)//2):
                if A > i >= 0 and B > j >= 0:
                    dictionary[(i, j)] -= 1
#这里能够使用减一的原因在于，不可能将相同大小的位置全部不行，因为碉堡只会出现在所有矩阵交集位置，让这个位置全部减一是不可能的
#这样就否定了该处存在碉堡了
max_can = max(dictionary.values())
count = 0
for value in dictionary.values():
    if value == max_can:
        count += 1

print(count)
from collections import defaultdict

d = defaultdict(int)
nums = list(map(int, input().split()))
for num in nums:
    d[num] += 1

max_vote = max(d.values())
winners = sorted([k for k, v in d.items() if v == max_vote])
print(' '.join(map(str, winners)))
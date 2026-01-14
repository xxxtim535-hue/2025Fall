n = int(input())
answer = []

while n:
    temp = n % 8
    answer.append(temp)
    n = n // 8

print(''.join(map(str, reversed(answer))))
n = int(input().strip())
name = {}
for _ in range(n):
    a, b = input().split("-")
    num = float(b[:-1]) * (1e6 if b[-1] == 'M' else 1e9)
    if a not in name:
        name[a] = []
    name[a].append((num, b))

sorted_name = dict(sorted(name.items()))
for nam in sorted_name.keys():
    sorted_num = sorted(sorted_name[nam], key=lambda x: x[0])
    print(f'{nam}: {", ".join(c for _, c in sorted_num)}')


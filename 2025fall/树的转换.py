char = input().strip()
count = 0
tree = {0: [[], None, 0]}
height = 0
mheight = 0
node = 0
for a in char:
    if a == "d":
        height += 1
        if height > mheight:
            mheight = height
        count += 1
        tree[count] = [[], 0, 0]
        tree[count][1] = node
        tree[node][0].append(count)
        tree[node][2] += 1
        node = count
    else:
        height -= 1
        node = tree[node][1]
def find_h(a):
    if not tree[a][0]:
        return 0
    n = len(tree[a][0])
    nheight = n
    for i, node in enumerate(tree[a][0]):
        height = i+1 + find_h(node)
        if height > nheight:
            nheight = height

    return nheight
nheight = find_h(0)

print(f"{mheight} => {nheight}")
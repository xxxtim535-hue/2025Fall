def traverse(x, tree):
    group = [x] + tree[x]
    for val in sorted(group):
        if val == x:
            print(x)
        else:
            traverse(val, tree)

n =  int(input())
tree = {}
all_children = set()

for _ in range(n):
    line = list(map(int, input().split()))
    val = line[0]
    tree[val] = line[1:]
    all_children.update(line[1:])

root = (set(tree.keys()) - all_children).pop()

traverse(root, tree)

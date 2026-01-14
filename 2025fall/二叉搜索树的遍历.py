import sys

def get_(preorder):
    if not preorder:
        return []

    root = preorder[0]

    left = [x for x in preorder[1:] if x < root]
    right = [x for x in preorder[1:] if x > root]

    return get_(left) + get_(right) + [root]

input = sys.stdin.readline
n = int(input())

preorder = list(map(int, input().split()))

postorder = get_(preorder)

print(" ".join(map(str, postorder)))
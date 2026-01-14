import sys用法

for line in sys.stdin:
    preorder, inorder = line.split()


    def build(pre_str, in_str):
        if not pre_str: return ""
        root = pre_str[0]
        idx = in_str.index(root)
        left = build(pre_str[1:idx + 1], in_str[:idx])
        right = build(pre_str[idx + 1:], in_str[idx + 1:])
        return left + right + root


    print(build(preorder, inorder))
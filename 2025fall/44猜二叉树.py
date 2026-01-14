from collections import deque


def solve():
    n = int(input())
    for _ in range(n):
        inorder = input().strip()
        postorder = input().strip()

        # 直接构建层次遍历序列，不显式建树
        queue = deque([(inorder, postorder)])
        result = []

        while queue:
            in_seq, post_seq = queue.popleft()
            if not post_seq:
                continue

            root = post_seq[-1]
            result.append(root)

            root_index = in_seq.index(root)
            left_in = in_seq[:root_index]
            right_in = in_seq[root_index + 1:]
            left_post = post_seq[:len(left_in)]
            right_post = post_seq[len(left_in):-1]

            if left_in:
                queue.append((left_in, left_post))
            if right_in:
                queue.append((right_in, right_post))

        print(''.join(result))


if __name__ == "__main__":
    solve()
def build_tree(inorder, postorder):
    if not inorder:
        return None

    root = {'val': postorder[-1], 'left': None, 'right': None}
    idx = inorder.index(postorder[-1])
    root['left'] = build_tree(inorder[:idx], postorder[:idx])
    root['right'] = build_tree(inorder[idx+1:], postorder[idx:-1])

    return root
def answer(root):
    result = []
    q = deque([root])
    while q:
        n = q.popleft()
        result.append(n['val'])
        if n['left']: q.append(n["left"])
        if n['right']: q.append(n["right"])

    return ''.join(result)
def main():
    n = int(input())
    for _ in range(n):
        inorder = input().strip()
        postorder = input().strip()
        root = build_tree(inorder, postorder)
        print(answer(root))
if __name__ == "__main__":
    main()



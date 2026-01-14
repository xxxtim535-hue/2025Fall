def parse_tree(s):
    """
    解析括号嵌套树字符串，返回 (root, children_dict)
    """
    if not s:
        return None, {}

    root = s[0]  # 根节点
    children_dict = {root: []}

    if len(s) > 1 and s[1] == '(':
        # 有子节点
        pos = 2  # 跳过 root 和 '('
        level = 0
        start = pos

        while pos < len(s):
            if s[pos] == '(':
                level += 1
            elif s[pos] == ')':
                if level == 0:
                    # 当前子树结束
                    subtree_str = s[start:pos]
                    if subtree_str:
                        child_root, child_children = parse_tree(subtree_str)
                        children_dict[root].append(child_root)
                        children_dict.update(child_children)
                    break
                else:
                    level -= 1
            elif s[pos] == ',' and level == 0:
                # 兄弟节点分隔
                subtree_str = s[start:pos]
                if subtree_str:
                    child_root, child_children = parse_tree(subtree_str)
                    children_dict[root].append(child_root)
                    children_dict.update(child_children)
                start = pos + 1
            pos += 1
    else:
        # 单节点，无子节点
        pass

    return root, children_dict


def preorder(root, children_dict):
    """前序遍历"""
    result = [root]
    for child in children_dict[root]:
        result.extend(preorder(child, children_dict))
    return result


def postorder(root, children_dict):
    """后序遍历"""
    result = []
    for child in children_dict[root]:
        result.extend(postorder(child, children_dict))
    result.append(root)
    return result


def main():
    s = input().strip()
    root, children_dict = parse_tree(s)

    pre = ''.join(preorder(root, children_dict))
    post = ''.join(postorder(root, children_dict))

    print(pre)
    print(post)


if __name__ == "__main__":
    main()


栈：

def build_tree_with_stack_robust(s):
    """更健壮的栈实现"""
    stack = []  # 保存当前节点
    children_dict = {}
    root = None
    i = 0
    n = len(s)

    while i < n:
        if s[i].isupper():
            # 处理节点名（可能有多字符，但题目说单个大写字母）
            node = s[i]
            children_dict[node] = []

            if not root:
                root = node
            elif stack:  # 栈非空时，栈顶是父节点
                parent = stack[-1]
                children_dict[parent].append(node)

            i += 1

        elif s[i] == '(':
            # 确保前面有节点
            if i > 0 and s[i - 1].isupper():
                stack.append(s[i - 1])
            i += 1

        elif s[i] == ')':
            if stack:
                stack.pop()
            i += 1

        elif s[i] == ',':
            i += 1

        else:
            # 跳过未知字符
            i += 1

    return root, children_dict
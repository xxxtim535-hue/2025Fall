import sys用法


class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = []  # 子目录列表
        self.files = []  # 文件列表


def main():
    # 读取所有输入
    data = sys.stdin.read().splitlines()
    datasets = []
    current_set = []

    # 分割数据集
    for line in data:
        line = line.strip()
        if not line:  # 跳过空行
            continue
        if line == '#':
            break
        if line == '*':
            if current_set:
                datasets.append(current_set)
                current_set = []
        else:
            current_set.append(line)

    # 处理最后一个数据集（如果存在）
    if current_set:
        datasets.append(current_set)

    # 处理每个数据集
    for idx, dataset in enumerate(datasets, 1):
        # 构建目录树
        root = Directory("ROOT")
        stack = [root]  # 栈用于跟踪当前目录

        for item in dataset:
            if item == ']':
                # 结束当前目录，返回上一级
                if len(stack) > 1:
                    stack.pop()
            elif item.startswith('d'):
                # 创建新目录
                new_dir = Directory(item)
                # 将新目录添加到当前目录的子目录列表中
                stack[-1].subdirs.append(new_dir)
                # 进入新目录
                stack.append(new_dir)
            else:
                # 文件（以f开头或直接是文件名）
                # 将文件添加到当前目录的文件列表中
                stack[-1].files.append(item)

        # 输出结果
        print(f"DATA SET {idx}:")
        print("ROOT")

        # 递归打印目录结构
        def print_structure(directory, level):
            indent = "|     " * level

            # 先打印子目录（按输入顺序）
            for subdir in directory.subdirs:
                print(f"{indent}{subdir.name}")
                print_structure(subdir, level + 1)

            # 再打印文件（按字母顺序排序）
            for file_name in sorted(directory.files):
                print(f"{indent}{file_name}")

        # 从根目录开始打印，层级为1
        print_structure(root, 1)

        # 在数据集之间输出空行（最后一个数据集后不输出）
        if idx < len(datasets):
            print()


if __name__ == "__main__":
    main()
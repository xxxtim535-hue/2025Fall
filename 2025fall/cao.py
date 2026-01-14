x = "global"  # 全局


def outer():
    x = "enclosing"  # 闭包

    def inner():
        x = "local"  # 局部
        print(x)  # 查找过程：
        # 1. Local: 找到"local" → 停止查找

    def inner2():
        print(x)  # 查找过程：
        # 1. Local: 没有x
        # 2. Enclosing: 找到outer的x="enclosing" → 停止

    def inner3():
        print(len)  # 查找过程：
        # 1. Local: 没有
        # 2. Enclosing: 没有
        # 3. Global: 没有（全局作用域没定义len）
        # 4. Built-in: 找到内置函数len → 停止

    inner()
    inner2()
    inner3()

outer()
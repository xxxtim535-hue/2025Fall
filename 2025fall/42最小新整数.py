t = int(input().strip())
results = []

for _ in range(t):
    data = input().split()
    n_str = data[0]
    k = int(data[1])

    stack = []
    for digit in n_str:
        # 当栈不为空，且还有删除名额，且当前数字小于栈顶数字时，弹出栈顶数字（删除）
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # 如果还有剩余的删除名额，从末尾删除（因为栈中数字已非递减）
    if k > 0:
        stack = stack[:-k]

    # 将栈中数字连接成字符串，并去除前导零（但题目保证数字不含0，所以可省略）
    result = ''.join(stack).lstrip('0')
    # 如果结果为空，输出0（但题目保证删除后位数至少为1，所以不会为空）
    if result == '':
        result = '0'
    results.append(result)

for res in results:
    print(res)
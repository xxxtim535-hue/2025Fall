n = int(input())
for _ in range(n):
    stack = []
    List = input().split()
    for string in List:
        if string in "+-*/":
            left = stack.pop()
            right = stack.pop()
            if string == "+":
                stack.append(right + left)
            elif string == "-":
                stack.append(right - left)
            elif string == "*":
                stack.append(right * left)
            elif string == '/':
                stack.append(right / left)
        else:
            stack.append(float(string))

    print(f"{stack[0]:.2f}")

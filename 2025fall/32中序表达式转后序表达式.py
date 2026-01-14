def answer(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    answer = []
    number = ''

    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        else:
            if number:
                answer.append(number)
                number = ''
            if char in '+-*/':
                while stack and stack[-1] in '+-*/' and precedence[char] <= precedence[stack[-1]]:
                    answer.append(stack.pop())
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    answer.append(stack.pop())
                stack.pop()

    if number:
        answer.append(number)

    while stack:
        answer.append(stack.pop())

    return " ".join(x for x in answer)


n = int(input())
for _ in range(n):
    expression = input()
    print(answer(expression))
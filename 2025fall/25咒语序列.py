string = input()
stack = list()
max_zi = 0
list_i = []
for i, chrac in enumerate(string):
    if chrac == ")":
        if stack:
            stack.pop()
        else:
            list_i.append(i)
    else:
        stack.append((i, chrac))

list_j = [t[0] for t in stack]
result = list_i + list_j
if not result:
    print(len(string))
else:
    m = len(result)
    for i in range(0, m-1):
        max_zi = max(max_zi, result[i+1]-result[i]-1)
    max_zi = max(max_zi, len(string) - 1 - result[-1])


    print(max_zi)



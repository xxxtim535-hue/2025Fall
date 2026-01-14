text = input().strip()
target = "hello"
index = 0
length = 5

for char in text:
    if char == target[index]:
        index += 1
    if index == length:
        print("YES")
        break

if index < length:
    print("NO")
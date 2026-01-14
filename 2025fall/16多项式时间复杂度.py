complicate = input().split("+")
num = []
for word in complicate:
    if word[0] != "0":
        indexnum = word.index("^")
        num.append(int(word[indexnum+1:]))
print(f"n^{max(num)}")


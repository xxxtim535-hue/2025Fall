s = input()

vowels = "AYEIOUaeyiou"

result = ""

for char in s:
    if char not in vowels:
        result += '.' + char.lower()

print(result)
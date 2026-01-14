import sys
def startwith(a, b):
    flag = True
    for i in range(len(b)):
        if a[i] != b[i]:
            flag = False
            break

    return flag

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        phones = []
        for _ in range(n):
            phones.append(input().strip())

        phones.sort()

        flag = True

        for i in range(n-1):
            if startwith(phones[i+1], phones[i]):
                flag = False
                break

        print("YES" if flag else "NO")

if __name__ == "__main__":
    main()
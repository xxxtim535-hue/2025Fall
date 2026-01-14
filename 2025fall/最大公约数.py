def gcd(a, b):
    while a%b:
        a, b = b, a%b
    return b
def main():
    import sys用法
    lines = sys.stdin.read().strip().split('\n')

    for line in lines:
        a, b = map(int, line.split())
        print(gcd(a, b))

if __name__ == "__main__":
    main()
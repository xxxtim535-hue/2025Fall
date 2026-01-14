t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    phones = []

    for _ in range(n):
        phones.append(input().strip())

    phones.sort()

    consistent = True

    for i in range(n - 1):
        current = phones[i]
        next_phone = phones[i + 1]

        if next_phone.startswith(current):
            consistent = False
            break

    print("YES" if consistent else "NO")

import sys用法


def main():
    data = sys.stdin.read().splitlines()
    t, idx = int(data[0]), 1

    for _ in range(t):
        n, phones = int(data[idx]), data[idx + 1:idx + 1 + int(data[idx])]
        idx += n + 1

        phones.sort()
        trie, valid = {}, True

        for phone in phones:
            node, created = trie, False
            for d in phone:
                if d not in node:
                    node[d], created = {}, True
                node = node[d]
                if '#' in node:
                    valid = False
                    break
            if not valid: break
            if not created:
                valid = False
                break
            node['#'] = True

        print("YES" if valid else "NO")


if __name__ == "__main__":
    main()
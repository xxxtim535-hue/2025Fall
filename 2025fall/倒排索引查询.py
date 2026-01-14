import sys用法

def main():
    data = sys.stdin.read().strip().split()
    p = 0
    N = int(data[p]);p+=1

    index = []
    all_docs = set()
    for _ in range(N):
        k = int(data[p]);p+=1
        docs = set()
        for _ in range(k):
            doc = int(data[p]);p += 1
            docs.add(doc)
            all_docs.add(doc)
        index.append(docs)

    m = int(data[p]);p+=1
    out = []

    for _ in range(m):
        cond = list(map(int, data[p:p+N]));p += N
        res = []
        for doc in all_docs:
            ok = True
            for i in range(N):
                c = cond[i]
                if c == 1 and doc not in index[i]:
                    ok = False
                    break
                if c == -1 and doc in index[i]:
                    ok = False
                    break
            if ok:
                res.append(doc)
        if res:
            res.sort()
            out.append(' '.join(map(str, res)))
        else:
            out.append("NOT FOUND")

    print('\n'.join(out))

if __name__ == "__main__":
    main()


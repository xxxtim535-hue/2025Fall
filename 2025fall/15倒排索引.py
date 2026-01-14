from collections import defaultdict

N = int(input().strip())

inverted_index = defaultdict(set)

for doc_id in range(1, N + 1):
    line = input().split()
    ci = int(line[0])
    words = line[1:1 + ci]

    for word in words:
        inverted_index[word].add(doc_id)

M = int(input().strip())

for _ in range(M):
    query_word = input().strip()
    if query_word in inverted_index:
        doc_list = sorted(inverted_index[query_word])
        print(' '.join(map(str, doc_list)))
    else:
        print("NOT FOUND")
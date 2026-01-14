def main():
    p = int(input())
    places = []
    placeind = {}
    for _ in range(p):
        place = input().strip()
        places.append(place)
        placeind[place] = _

    INF = float('inf')
    dist = [[INF] * p for _ in range(p)]
    next_node = [[-1] * p for _ in range(p)]

    for i in range(p):
        dist[i][i] = 0

    q = int(input())
    for _ in range(q):
        a, b, d = input().strip().split()
        u, v = placeind[a], placeind[b]
        d_val = int(d)
        dist[u][v] = d_val
        dist[v][u] = d_val
        next_node[u][v] = v

    for k in range(p):
        for i in range(p):
            for j in range(p):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    r = int(input())
    results = []
    for _ in range(r):
        a, b = input().split()
        u, v = placeind[a], placeind[b]

        if dist[u][v] == INF:
            results.append(f"{a}->(不可达)->{b}")
        else:
            path = []
            cur = u
            while cur != v:
                path.append(places[cur])
                nxt = next_node[cur][v]
                path.append(f"({dist[cur][nxt]})")
                cur = nxt
            path.append(places[v])
            results.append("->".join(path))
            
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
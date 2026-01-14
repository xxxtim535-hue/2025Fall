import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:  # 关键判断
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def prim(graph):
    n = len(graph)
    in_mst = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    pq = [(0, 0)]
    res = 0

    while pq:
        w, u = heapq.heappop(pq)
        if in_mst[u] or w > min_edge[u]:
            continue
        in_mst[u] = True
        res += w
        for v, weight in graph[u]:
            if not in_mst[v] and weight < min_edge[v]:
                min_edge[v] = weight
                heapq.heappush(pq, (weight, v))

    return res
import heapq

def dijkstras(V, adj, start):
    dist = [float('inf')] * V
    dist[start] = 0
    # print(dist)
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        d, node = heapq.heappop(pq)

        if d>dist[node]:
            continue

        for i, j in adj[node]:
            if(dist[i] > dist[node]+j):
                dist[i] = dist[node]+j
                heapq.heappush(pq, (dist[i], i))

    return dist

V = 5
adj = [
    [[1, 4], [2, 8]],         
    [[0, 4], [4, 6], [2,3]], 
    [[0, 8], [3, 2], [1,3]], 
    [[2, 2], [4, 10]], 
    [[1, 6], [3, 10]]
    ]

print(dijkstras(V, adj, 0))
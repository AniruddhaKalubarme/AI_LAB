import heapq

def Astar(adj, n, h, start, goal):
    dist = [float('inf')] * n
    dist[start] = 0
    parent = [-1] * n

    pq = []
    heapq.heappush(pq, (h[start], start))   

    while pq:
        fn, node = heapq.heappop(pq)

        if node == goal:
            break
        
        #optional
        if fn > dist[node] + h[node]:
            continue

        for neighbor, weight in adj[node]:
            gn = dist[node] + weight

            if gn < dist[neighbor]:
                dist[neighbor] = gn
                fn = gn + h[neighbor]
                heapq.heappush(pq, (fn, neighbor))
                parent[neighbor] = node

    return dist, parent

n = 4
adj = [
    [[1,1],[2,3]],
    [[2,1],[3,5]],
    [[3,3]],
    []
]

h = [4,1,2,0]

dist, parent = Astar(adj, n, h, 0, 3)

print(dist, parent)
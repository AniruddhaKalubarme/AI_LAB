
def Prims(start, adj, visited, dist, parent, n):
    dist[start] = 0

    for i in range (0, n):
        index = -1
        iMin = 1000
        for j in range (0, n):
            if(visited[j] == False and dist[j]<iMin):
                index = j
                iMin = dist[j]
        
        visited[index] = True

        for j in adj[index]:
            neighbor = j[0]
            weight = j[1]
            if(visited[neighbor] == False and dist[neighbor]>weight):
                dist[neighbor] = weight
                parent[neighbor] = index


n = 3
visited = [False]*n
parent = [-1]*n
dist = [1000]*n
adj = [
    [[1,5],[2,1]],
    [[0,5],[2,3]],
    [[0,1],[1,3]]
]

Prims(0, adj, visited, dist, parent, n)
print(parent)
print(dist)


from collections import deque

def bfs(start, adj, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while(q):
        # print(q)
        # ---------------------------------
        x = q.popleft()
        # -----------------------------------
        print(x, end=" -> ")
        for i in adj[x]:
            if(visited[i] == False):
                q.append(i)
                visited[i] = True


adj = [[1,2], [0,2], [0,1,3,4], [2], [2]]
visited = [False for _ in range(0, len(adj))]
bfs(0, adj, visited)

def dfs(n, visited, adj):
    print(n, end=" -> ")
    visited[n] = True
    for i in adj[n]:
        if(visited[i] == False):
            dfs(i, visited, adj)

n = int(input("Enter the number of Vertices: "))
# adj = [[2,3,1],[0],[0,4],[0],[2]]
adj = []
visited = [False for _ in range (0, n)]

for i in range(0,n):
    lis = []
    print(f"adjecents of {i}")

    while(True):
        k=int(input("Enter the adj: "))
        if(k == -1):
            break
        lis.append(k)
    adj.append(lis)


# print(adj)
dfs(0, visited, adj)

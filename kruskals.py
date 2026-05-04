def findParent(node, parent):
    if(parent[node] == node):
        return node
    
    parent[node] = findParent(parent[node], parent)
    return parent[node]

def Union(u, v, parent, rank):
    u = findParent(u, parent)
    v = findParent(v, parent)

    if(rank[u] < rank[v]):
        parent[u] = v
    elif(rank[v] < rank[u]):
        parent[v] = u
    else:
        parent[v] = u
        rank[u] = rank[u] + 1


V = 6
rank = [0] * V
parent = [i for i in range(0, V)]
edges = [[0,1,5], [0,3,1], [1,2,8], [1,4,3], [2,3,4], [2,5,2], [3,4,3], [4,5,6]]
edges.sort(key=lambda x: x[2])
weight = 0

for i in edges:
    u = findParent(i[0], parent)
    v = findParent(i[1], parent)
    w = i[2]

    if(u != v):
        
        weight += w
        Union(u, v, parent, rank)


print("weight of MST is : ", weight)

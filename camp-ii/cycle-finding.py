n, m = map(int, input().split())

edges = []
graph = [[] for _ in range(n+1)]
neg = 0

for _ in range(m):
    u, v, d = map(int, input().split())
    if d < 0:
        neg += 1
    edges.append((u, v, d))
    graph[u].append((v, d))  
    
if neg == 0:
    print('NO')
    exit()  
    
dist = [float('inf')] * (n+1)
prev = [None] * (n+1)
  
idx = 1  
C = -1

while C == -1 and idx <= n:
    dist[idx] = 0
    for _ in range(n):
        for u, v, d in edges:
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                prev[v] = u             
    
    for u, v, d in edges:
        if dist[v] > dist[u] + d:
            C = u
            break
            
    while idx <= n and dist[idx] != float('inf'):
        idx += 1 
        
# print(dist)    
if C == -1:
    print('NO')
else:
    for _ in range(n):
        C = prev[C]
        
    path = [C, prev[C]]
    while path[0] != path[-1]:
        path.append(prev[path[-1]])
        
    print('YES')
    print(*reversed(path))
    


    

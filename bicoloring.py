def dfs(node, color, colors, graph):
    colors[node] = color
    nextCol = 3 - color

    for adj in graph[node]:
        if colors[adj] == color:
            return False
        if colors[adj] == 0 and not dfs(adj, nextCol, colors, graph):
            return False
    
    return True

while True:
    n = int(input())
    if n == 0:
        break

    graph = [[] for _ in range(n+1)]
    colors = [0] * (n+1)

    for _ in range(int(input())):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    res = dfs(1, 1, colors, graph)
    print("BICOLOURABLE." if res else "NOT BICOLOURABLE.")

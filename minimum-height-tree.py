class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0] * n
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        currLevel = []
        for node in range(n):
            if degree[node] <= 1:
                currLevel.append(node)

        while True:
            nextLevel = []
            for node in currLevel:
                for child in graph[node]:
                    degree[child] -= 1
                    if degree[child] == 1:
                        nextLevel.append(child)

            if not nextLevel:
                break
            currLevel = nextLevel

        return currLevel

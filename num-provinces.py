class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adjList = [[] for _ in range(n)]

        for row in range(n):
            for col in range(row+1, n):
                if isConnected[row][col] == 1:
                    adjList[row].append(col)
                    adjList[col].append(row)

        visited = set()

        def dfs(city):
            visited.add(city)
            for neighbor in adjList[city]:
                if neighbor not in visited:
                    dfs(neighbor)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for end1, end2 in edges:
            graph[end1].append(end2)
            graph[end2].append(end1)

        visited = set()

        def dfs(node):
            visited.add(node)
            res = 0

            for adj in graph[node]:
                if adj not in visited:
                    temp = dfs(adj)
                    res += temp
                    if temp > 0 or hasApple[adj]:
                        res += 2

            return res

        return dfs(0)


        
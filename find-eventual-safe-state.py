class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        seen = [0] * len(graph)
        res = []

        def dfs(node):
            seen[node] = 1

            for child in graph[node]:
                if seen[child] == 2:
                    continue
                if seen[child] == 1:
                    return False
                if seen[child] == 0:
                    if not dfs(child):
                        return False

            seen[node] = 2
            res.append(node)
            return True        

        for node in range(len(graph)):
            if seen[node] == 0:
                dfs(node)
        return sorted(res)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []

        def dfs(curr, node):
            curr.append(node)
            if node == n-1:
                res.append(curr.copy())
                curr.pop()
                return

            for next_node in graph[node]:
                dfs(curr, next_node)
            curr.pop()

        dfs([], 0)
        return res

            

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]

        for end1, end2 in edges:
            graph[end1].append(end2)
            graph[end2].append(end1)

        res = [0] * n
        count = [0] * 26

        def dfs(node, parent):
            idx = ord(labels[node]) - ord('a')
            before = count[idx]
            count[idx] += 1

            for child in graph[node]:
                if child != parent:
                    dfs(child, node)

            res[node] = count[idx] - before

        dfs(0, -1)
        return res

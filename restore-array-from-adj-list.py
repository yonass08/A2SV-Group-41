class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        start = 0

        for node in graph:
            if len(graph[node]) == 1:
                start = node

        res = []

        def dfs(node, parent):
            res.append(node)

            for child in graph[node]:
                 if child != parent:
                     dfs(child, node)

        dfs(start, float('inf'))
        return res
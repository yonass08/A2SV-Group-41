class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        quiet_person = [0] * len(quiet)
        for i, q in enumerate(quiet):
            quiet_person[q] = i

        graph = [[] for _ in range(len(quiet))]

        for a, b in richer:
            graph[b].append(a)

        res = [len(quiet)] * len(quiet)
        seen = [False] * len(quiet)

        def dfs(node):
            seen[node] = True
            minq = quiet[node]

            for child in graph[node]:
                if seen[child]:
                    minq = min(minq, quiet[res[child]])
                else:
                    minq = min(minq, dfs(child))

            res[node] = quiet_person[minq]
            return minq

        for node in range(len(quiet)):
            if not seen[node]:
                dfs(node)

        return res


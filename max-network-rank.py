class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edgeset = set()

        degree = [0] * n
        for road in roads:
            edgeset.add((road[0], road[1]))
            degree[road[0]] += 1
            degree[road[1]] += 1

        res = 0
        for i in range(n):
            for j in range(i+1, n):
                curr = degree[i] + degree[j] - int((i, j) in edgeset or (j, i) in edgeset)
                res = max(res, curr)

        return res
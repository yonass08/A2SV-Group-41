class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)

        def dist(i, j):
            return (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                if dist(i, j) <= bombs[i][2]**2:
                    adj[i].append(j)
                if dist(i, j) <= bombs[j][2]**2:
                    adj[j].append(i)

        def dfs(i, visited):
            visited.add(i)
            count = 1

            for child in adj[i]:
                if child not in visited:
                    count += dfs(child, visited)

            return count

        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))

        return res

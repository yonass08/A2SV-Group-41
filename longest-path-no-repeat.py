class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        res = 0
        graph = [[] for _ in range(len(s))]

        for i in range(1, len(s)):
            graph[parent[i]].append(i)

        def dfs(root):
            nonlocal res
            max1, max2 = 0, 0

            for child in graph[root]:
                count, char = dfs(child)
                if char != s[root]:
                    if count >= max1:
                        max2 = max1
                        max1 = count
                    elif count > max2:
                        max2 = count

            res = max(res, max1 + max2 + 1)
            return max1 + 1, s[root]

        dfs(0)
        return res

        

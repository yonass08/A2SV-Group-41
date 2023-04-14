class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dirns = [1, 0, -1, 0, 1]
        m, n = len(grid1), len(grid1[0])
        isInbound = lambda row, col: 0 <= row < m and 0 <= col < n

        def dfs(row, col):
            if (not isInbound(row, col)) or grid2[row][col] == 0:
                return True

            res = True
            grid2[row][col] = 0

            for i in range(4):
                temp = dfs(row + dirns[i], col + dirns[i+1])
                res = res and temp

            return res and grid1[row][col] == 1

        res = 0

        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1 and grid1[row][col] != 0:
                    res += dfs(row, col)

        return res

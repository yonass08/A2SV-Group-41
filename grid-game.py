class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1:
            return 0

            
        for i in range(1, n):
            grid[1][i] += grid[1][i-1]

        for i in range(n-2, -1, -1):
            grid[0][i] += grid[0][i+1]

        res = min(grid[0][1], grid[1][n-2])

        for i in range(n-2):
            res = min(res, max(grid[1][i], grid[0][i+2]))

        return res

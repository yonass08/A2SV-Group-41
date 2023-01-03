class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        res = []
        colDiff = []

        for row in range(m):
            rowSum = sum(grid[row])
            res.append([2*rowSum - n] * n)

        for col in range(n):
            colSum = 0
            for row in range(m):
                colSum += grid[row][col]

            colDiff = 2 * colSum - m
            for row in range(m):
                res[row][col] += colDiff

        return res




        

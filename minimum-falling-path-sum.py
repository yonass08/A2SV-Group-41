class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        def ans(row, col):
            res = matrix[row-1][col]
            if col > 0:
                res = min(res, matrix[row-1][col-1])
            if col < n-1:
                res = min(res, matrix[row-1][col+1])

            return res

        for row in range(1, n):
            for col in range(n):
                matrix[row][col] += ans(row, col)

        return min(matrix[-1])
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        res = [[0] * (cols-2) for _ in range(rows-2)]

        for row in range(rows-2):
            for col in range(cols-2):
                res[row][col] = max(grid[row][col],
                                grid[row][col+1],
                                grid[row][col+2],
                                
                                grid[row+1][col],
                                grid[row+1][col+1],
                                grid[row+1][col+2],

                                grid[row+2][col],
                                grid[row+2][col+1],
                                grid[row+2][col+2]
                                )

        return res



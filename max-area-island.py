class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        dirn = [1, 0, -1, 0, 1]
        isInbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def process(row, col):
            if not isInbound(row, col) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            
            count = 1
            for i in range(4):
                count += process(row+dirn[i], col+dirn[i+1])

            return count

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(res, process(row, col))

        return res

    
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        queue = deque([(0, 0)])
        grid[0][0] = 1

        dirns =  [1, 0, -1, 0, 1, -1, -1, 1]
        res = 0

        isInbound = lambda row, col: 0 <= row < n and 0 <= col < n

        while queue:
            res += 1
            for i in range(len(queue)):
                row, col = queue.popleft()
                if row == col == n-1:
                    return res

                
                for i in range(-1, 7):
                    n_row = row + dirns[i]
                    n_col = col + dirns[i+1]

                    if isInbound(n_row, n_col) and grid[n_row][n_col] == 0:
                        queue.append((n_row, n_col))
                        grid[n_row][n_col] = 1

        return -1
                


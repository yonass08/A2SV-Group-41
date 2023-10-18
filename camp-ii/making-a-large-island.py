class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dirns = [1, 0, -1, 0, 1]
        
        isInbound = lambda row, col:  0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col , color):
            grid[row][col] = color
            res = 1
            
            for i in range(4):
                nrow, ncol = row + dirns[i], col + dirns[i+1]
                
                if isInbound(nrow, ncol) and grid[nrow][ncol] == 1:
                    res += dfs(nrow, ncol, color)
                    
            return res
                    
        count = {}
        res = 0
                    
        color = 2
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count[color] = dfs(row, col, color)
                    res = max(res, count[color])
                    color += 1
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    continue
                    
                cur = 1
                notallowed = [0]
                
                for i in range(4):                        
                    nrow, ncol = row + dirns[i], col + dirns[i+1]
                    if isInbound(nrow, ncol) and grid[nrow][ncol] not in notallowed:
                        cur += count[grid[nrow][ncol]]
                        notallowed.append(grid[nrow][ncol])

                res = max(res, cur)
                    
        return res
                    
        
        
                    
            
            
        
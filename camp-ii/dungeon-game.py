class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [[0] * n for _ in range(m)]
        
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                prev = float('inf')
                
                if row+1 < m:
                    prev = min(prev, dp[row+1][col])
                    
                if col+1 < n:
                    prev = min(prev, dp[row][col+1])
                    
                if prev == float('inf'):
                    dp[row][col] = max(0, 1 - dungeon[row][col])
                else:
                    dp[row][col] = max(0, 1 - dungeon[row][col], prev - dungeon[row][col])
                    
        return max(1, dp[0][0])
                    
                
        
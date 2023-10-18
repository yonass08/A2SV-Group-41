class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        small = min(m, n) - 1
        big = max(m, n) - 1
        
        res = 1
        
        for num in range(big+1, small + big + 1):
            res *= num
            
        for num in range(1, small + 1):
            res //= num
            
        return res
        
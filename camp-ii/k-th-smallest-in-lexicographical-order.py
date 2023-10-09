class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def helper(x): 
            res, diff = 0, 1
            while x <= n: 
                res += min(n - x + 1, diff)
                x *= 10 
                diff *= 10 
            return res 
        
        x = 1
        while k > 1: 
            count = helper(x)
            if k > count: k -= count; x += 1
            else: k -= 1; x *= 10 
                
        return x
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1/x
            
        curr = x
        
        res = 1
        
        while n:
            if n % 2 == 1:
                res *= curr
            n >>= 1
            curr *= curr
            
        return res
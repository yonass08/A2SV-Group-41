class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        curr = 2

        while n > 1:
            while n % curr == 0:
                res += curr
                n //= curr
            curr += 1
        
        return res
    

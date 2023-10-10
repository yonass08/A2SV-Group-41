class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res = 0
        curr = []
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        def backtrack(seen):
            nonlocal res
            
            first = 0
            while seen >> first & 1 == 1:
                first += 1
                
            if first == len(nums):
                sor = sorted(curr)
                val = sum((i+1) * num for i, num in enumerate(sor))
                res = max(res, val)
                
            seen |= 1 << first
            for i in range(len(nums)):
                if seen >> i & 1 == 1:
                    continue
                    
                curr.append(gcd(nums[first], nums[i]))
                seen |= 1 << i
                backtrack(seen)
                seen ^= 1 << i
                curr.pop()
                
            seen ^= 1 << first
            
        backtrack(0)
        return res
            
                
        
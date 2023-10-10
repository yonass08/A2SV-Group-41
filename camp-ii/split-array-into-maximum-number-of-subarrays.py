class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        And = [0] * len(nums)
        And[-1] = nums[-1]
        
        for i in range(len(nums)-2, -1, -1):
            And[i] = nums[i] & And[i+1]
                        
        if And[0] != 0:
            return 1
        
        base = 2 ** 20 - 1
        And.append(0)
        curr = base
        res  = 0
        
        for i in range(len(nums)):
            curr &= nums[i]
            if curr == 0 and And[i+1] == 0:
                res += 1
                curr = base
                
        return res
        
        
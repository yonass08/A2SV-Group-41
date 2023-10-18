class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        
        @cache
        def dp(curr, idx):
            if curr == 0:
                return True
            
            if idx >= len(nums):
                return False
            
            return dp(curr, idx + 1) or dp(curr - nums[idx], idx + 1)
        
        return dp(tot // 2, 0)
        
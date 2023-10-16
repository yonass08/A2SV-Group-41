class Solution:
    def minOperations(self, nums: List[int]) -> int:
        width = len(nums)
        nums = sorted(set(nums))
        
        res = width
        
        right = 0
        for left in range(len(nums)):
            while right < len(nums) and nums[right] <= nums[left] + width - 1:
                right += 1
                
            res = min(res, width - right + left)
            
        return res
                
            
                
            
            
        
        
        
        
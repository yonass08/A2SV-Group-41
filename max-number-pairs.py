class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        left, right = 0, len(nums)-1
        nums.sort()
        
        while left < right:
            if nums[left] + nums[right] == k:
                result += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
            
        return result

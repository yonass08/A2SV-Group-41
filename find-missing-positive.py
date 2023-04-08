class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]

        res = len(nums) + 1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                res = i+1
                break

        return res

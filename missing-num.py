class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = 0

        while curr < len(nums):
            curr_num = nums[curr]
            if curr_num == curr:
                curr += 1
            elif curr_num < len(nums):
                nums[curr], nums[curr_num] = nums[curr_num], nums[curr]
            else:
                curr += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)

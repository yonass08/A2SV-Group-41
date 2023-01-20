class Solution:
    def sortColors(self, nums):
        left, index, right = 0, 0, len(nums)-1

        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                index += 1
                left += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            

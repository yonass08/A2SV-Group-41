class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        curr = 0

        while curr < len(nums):
            curr_num = nums[curr]

            if curr_num == curr+1:
                curr += 1
            elif nums[curr_num-1] == curr_num:
                curr += 1
            else:
                nums[curr], nums[curr_num-1] = nums[curr_num-1], nums[curr]

        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)

        return res

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.roblist(nums[1:]), nums[0] + self.roblist(nums[2:-1]))

    def roblist(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            res.append(max(res[-2] + nums[i], res[-1]))

        return res[-1]

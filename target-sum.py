class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(idx, target):
            if idx == len(nums):
                return int(target == 0)

            if (idx, target) not in memo:
                memo[(idx, target)] = helper(idx+1, target-nums[idx]) + helper(idx+1, target+nums[idx])

            return memo[(idx, target)]

        return helper(0, target)
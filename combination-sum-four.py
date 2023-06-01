class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        smallest = min(nums)

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in range(smallest, target+1):
            for comb in nums:
                if num >= comb:
                    dp[num] += dp[num - comb]

        return dp[-1]



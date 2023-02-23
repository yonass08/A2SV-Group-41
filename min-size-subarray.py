class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1

        left = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return res if res <= len(nums) else 0
    
#30min
